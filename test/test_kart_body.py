"""Tests for the kart instance stat writes in game_state, using a fake dolphin
memory backend. Any read from an address that wasn't explicitly seeded raises,
which mirrors the invalid-read disconnects that real garbage pointers cause."""
import struct
import sys
import types
import unittest

# game_state imports dolphin_memory_engine at module level; stub it if the
# test environment doesn't have it installed. It gets replaced by FakeDolphin
# in the tests either way.
if "dolphin_memory_engine" not in sys.modules:
    sys.modules["dolphin_memory_engine"] = types.ModuleType("dolphin_memory_engine")

from .. import game_data, game_state, mem_addresses


class FakeDolphin:
    """Dict-backed game memory."""

    def __init__(self):
        self.mem: dict[int, bytes] = {}
        self.writes: list[tuple[int, bytes]] = []

    def seed_word(self, address: int, value: int):
        self.mem[address] = struct.pack(">I", value)

    def seed_byte(self, address: int, value: int):
        self.mem[address] = struct.pack(">B", value)

    def seed_float(self, address: int, value: float):
        self.mem[address] = struct.pack(">f", value)

    def _read(self, address: int, fmt: str):
        if address not in self.mem:
            raise RuntimeError(f"invalid read at {address:#x}")
        return struct.unpack(fmt, self.mem[address])[0]

    def read_word(self, address: int) -> int:
        return self._read(address, ">I")

    def read_byte(self, address: int) -> int:
        return self._read(address, ">B")

    def read_float(self, address: int) -> float:
        return self._read(address, ">f")

    def write_float(self, address: int, value: float):
        self.mem[address] = struct.pack(">f", value)
        self.writes.append((address, self.mem[address]))

    def write_bytes(self, address: int, value: bytes):
        self.mem[address] = value
        self.writes.append((address, value))

    def write_word(self, address: int, value: int):
        self.mem[address] = struct.pack(">I", value)
        self.writes.append((address, self.mem[address]))


KART_CTRL = 0x80400000
BODY = 0x80500000


class TestKartBodyStats(unittest.TestCase):
    def setUp(self):
        self.ma = mem_addresses.MkddMemAddressesUsa()
        self.fake = FakeDolphin()
        self._real_dolphin = game_state.dolphin
        game_state.dolphin = self.fake
        self.gs = game_state.MkddGameState(self.ma)
        self.gs.engine_upgrade_level = 1  # multiplier 1.0, keeps expectations simple

    def tearDown(self):
        game_state.dolphin = self._real_dolphin

    def seed_race(self, kart_id: int, mynum: int = 0, vehicle_class: int = 1):
        """Seeds the minimum memory for a running race with one kart body."""
        ma = self.ma
        self.fake.seed_word(ma.kart_control_pointer, KART_CTRL)
        self.fake.seed_word(KART_CTRL + ma.kart_control_kart_pointers_offset, BODY)
        self.fake.seed_word(BODY + ma.kart_body_setting_ptr_offset,
                            ma.kart_stats_pointer + kart_id * ma.kart_struct_size)
        self.fake.seed_byte(BODY + ma.kart_body_mynum_b_offset, mynum)
        self.fake.seed_byte(BODY + ma.kart_body_class_b_offset, vehicle_class)
        self.fake.seed_float(ma.class_speed_multipliers_fx + min(2, vehicle_class) * 4, 1.0)

    def as_float(self, value: float) -> float:
        """Rounds through single precision, like a write to game memory does."""
        return struct.unpack(">f", struct.pack(">f", value))[0]

    def test_not_in_game_reads_nothing(self):
        """Outside a race every read through the kart pointers is invalid and
        would disconnect the client. The function must not read at all."""
        self.gs.in_game = False
        self.gs.apply_player_kart_body_stats()  # any read would raise
        self.assertEqual(self.fake.writes, [])

    def test_player_body_gets_upgraded_stats(self):
        self.gs.in_game = True
        kart_id = self.gs.active_kart.id
        self.gs.kart_upgrades[kart_id] = [game_data.KART_UPGRADE_TURBO]
        self.seed_race(kart_id)

        self.gs.apply_player_kart_body_stats()

        stats = game_data.KARTS[kart_id].stats
        self.assertEqual(self.fake.read_float(BODY + self.ma.kart_body_speeds_fx_offset),
                         self.as_float(stats.speed_on_road))
        mini_turbo = struct.unpack(">H", self.fake.mem[BODY + self.ma.kart_body_mini_turbo_max_h_offset])[0]
        self.assertEqual(mini_turbo, int(1 + stats.mini_turbo + 30))
        self.assertEqual(self.fake.read_float(BODY + self.ma.kart_body_mass_f_offset),
                         self.as_float(stats.mass))

    def test_ghost_body_in_player_slot_is_skipped(self):
        """Issue #41 regression: during init the slot can hold the ghost's body
        (same kart id, mynum != 0). It must not receive the player's upgrades."""
        self.gs.in_game = True
        kart_id = self.gs.active_kart.id
        self.gs.kart_upgrades[kart_id] = [game_data.KART_UPGRADE_TURBO]
        self.seed_race(kart_id, mynum=1)

        self.gs.apply_player_kart_body_stats()

        self.assertEqual(self.fake.writes, [])

    def test_uninitialized_body_is_skipped(self):
        """A body whose stat table pointer is garbage must be left alone."""
        self.gs.in_game = True
        self.seed_race(self.gs.active_kart.id)
        self.fake.seed_word(BODY + self.ma.kart_body_setting_ptr_offset, 0xDEADBEEF)

        self.gs.apply_player_kart_body_stats()

        self.assertEqual(self.fake.writes, [])

    def test_wrong_kart_body_is_skipped(self):
        """A body driving a different kart than the player's must be left alone."""
        self.gs.in_game = True
        other_kart_id = (self.gs.active_kart.id + 1) % len(game_data.KARTS)
        self.seed_race(other_kart_id)

        self.gs.apply_player_kart_body_stats()

        self.assertEqual(self.fake.writes, [])
