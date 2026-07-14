"""
Tests for the cup unlock modes.
"""
from . import MkddTestBase
from worlds.mario_kart_double_dash import game_data, items as mkdd_items


def _pool_names(test_base) -> list:
    return [item.name for item in test_base.multiworld.itempool]


def _precollected_names(test_base) -> list:
    return [item.name for item in test_base.multiworld.precollected_items[test_base.player]]


class TestCupUnlocksShared(MkddTestBase):
    options = {"cup_unlocks": "shared"}

    def test_normal_cup_items(self) -> None:
        all_names = _pool_names(self) + _precollected_names(self)
        for cup in game_data.NORMAL_CUPS:
            self.assertEqual(all_names.count(cup), 1)
            self.assertNotIn(mkdd_items.get_item_name_cup_progressive(cup), all_names)
            for vehicle_class in range(4):
                self.assertNotIn(mkdd_items.get_item_name_cup_class(cup, vehicle_class), all_names)


class TestCupUnlocksProgressive(MkddTestBase):
    options = {"cup_unlocks": "progressive"}

    def test_progressive_cup_items(self) -> None:
        all_names = _pool_names(self) + _precollected_names(self)
        for cup in game_data.NORMAL_CUPS:
            self.assertNotIn(cup, all_names)
            self.assertEqual(all_names.count(mkdd_items.get_item_name_cup_progressive(cup)), 4)

    def test_one_progressive_cup_precollected(self) -> None:
        precollected = _precollected_names(self)
        count = sum(1 for cup in game_data.NORMAL_CUPS
                    if mkdd_items.get_item_name_cup_progressive(cup) in precollected)
        self.assertEqual(count, 1)


class TestCupUnlocksPerClass(MkddTestBase):
    options = {"cup_unlocks": "per_class"}

    def test_cup_class_items(self) -> None:
        all_names = _pool_names(self) + _precollected_names(self)
        for cup in game_data.NORMAL_CUPS:
            self.assertNotIn(cup, all_names)
            for vehicle_class in range(4):
                self.assertEqual(all_names.count(mkdd_items.get_item_name_cup_class(cup, vehicle_class)), 1)

    def test_a_50cc_cup_is_precollected(self) -> None:
        precollected = _precollected_names(self)
        count = sum(1 for cup in game_data.NORMAL_CUPS
                    if mkdd_items.get_item_name_cup_class(cup, 0) in precollected)
        self.assertEqual(count, 1)
