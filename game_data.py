from enum import IntEnum
from typing import NamedTuple

class Character(NamedTuple):
    id: int
    name: str
    weight: int
    default_kart: int
    item_offset: int

CHARACTERS = [
    Character(0, "Mario", 1, 8, 21),
    Character(1, "Luigi", 1, 9, 21),
    Character(2, "Peach", 1, 10, 14),
    Character(3, "Daisy", 1, 11, 14),
    Character(4, "Yoshi", 1, 12, 11),
    Character(5, "Birdo", 1, 13, 11),
    Character(6, "Baby Mario", 0, 0, 7),
    Character(7, "Baby Luigi", 0, 1, 7),
    Character(8, "Toad", 0, 6, 12),
    Character(9, "Toadette", 0, 7, 12),
    Character(10, "Koopa", 0, 2, 17),
    Character(11, "Paratroopa", 0, 3, 17),
    Character(12, "Donkey Kong", 2, 16, 4),
    Character(13, "Diddy Kong", 0, 4, 4),
    Character(14, "Bowser", 2, 17, 1),
    Character(15, "Bowser Jr.", 0, 5, 1),
    Character(16, "Wario", 2, 15, 8),
    Character(17, "Waluigi", 1, 14, 8),
    Character(18, "Petey Piranha", 2, 18, 8),
    Character(19, "King Boo", 2, 19, 8),
]

class KartStats(NamedTuple):
    speed_on_road: float
    speed_off_road_sand: float
    speed_off_road_grass: float
    speed_off_road_mud: float
    acceleration_1: float
    acceleration_2: float
    mini_turbo: float
    mass: float
    roll: float
    steer: float

class Kart(NamedTuple):
    id: int
    name: str
    weight: int
    unlock_id: int
    stats: KartStats

# Kart stats table based on work by Ralf.
#                Speed1    Speed2   Speed3   Speed4   Accel1    Accel2    Turbo     Mass    Roll   Steer
KARTS = [
    Kart(0, "Goo-Goo Buggy", 0, 5,
        KartStats(136.0,    116.0,    92.0,    20.0,    3.00,    0.010,    30.0,    1.25,    5.0,    2.0)),
    Kart(1, "Rattle Buggy", 0, 13,
        KartStats(137.0,    117.0,    92.0,    20.0,    2.00,    0.010,    30.0,    1.25,    5.0,    2.0)),
    Kart(2, "Koopa Dasher", 0, 3,
        KartStats(137.0,    117.0,    89.0,    20.0,    2.00,    0.010,    30.0,    1.50,    4.0,    2.0)),
    Kart(3, "Para-Wing", 0, 11,
        KartStats(136.0,    116.0,    89.0,    20.0,    3.00,    0.010,    30.0,    1.50,    4.0,    2.0)),
    Kart(4, "Barrel Train", 0, 9,
        KartStats(143.0,    123.0,    86.0,    20.0,    0.15,    0.005,    30.0,    2.00,    5.0,    0.9)),
    Kart(5, "Bullet Blaster", 0, 15,
        KartStats(143.0,    123.0,    68.0,    20.0,    0.30,    0.005,    30.0,    1.00,    5.0,    0.8)),
    Kart(6, "Toad Kart", 0, 16,
        KartStats(138.0,    118.0,    92.0,    20.0,    1.00,    0.010,    30.0,    1.25,    5.0,    3.0)),
    Kart(7, "Toadette Kart", 0, 17,
        KartStats(136.0,    116.0,    92.0,    20.0,    3.00,    0.010,    30.0,    1.25,    5.0,    3.0)),
    Kart(8, "Red Fire", 1, 0,
        KartStats(140.0,    120.0,    80.0,    20.0,    0.30,    0.005,    20.0,    2.00,    4.5,    1.0)),
    Kart(9, "Green Fire", 1, 8,
        KartStats(142.0,    122.0,    77.0,    20.0,    0.15,    0.005,    20.0,    1.75,    4.5,    1.0)),
    Kart(10, "Heart Coach", 1, 4,
        KartStats(139.0,    119.0,    83.0,    20.0,    1.00,    0.005,    20.0,    2.00,    5.0,    1.5)),
    Kart(11, "Bloom Coach", 1, 12,
        KartStats(141.0,    121.0,    77.0,    20.0,    0.50,    0.005,    20.0,    1.50,    5.0,    1.5)),
    Kart(12, "Turbo Yoshi", 1, 2,
        KartStats(139.0,    119.0,    80.0,    20.0,    1.00,    0.005,    20.0,    2.25,    4.5,    1.0)),
    Kart(13, "Turbo Birdo", 1, 10,
        KartStats(141.0,    121.0,    77.0,    20.0,    0.30,    0.005,    20.0,    2.50,    4.5,    1.0)),
    Kart(14, "Waluigi Racer", 1, 14,
        KartStats(140.0,    120.0,    92.0,    20.0,    0.50,    0.005,    20.0,    2.25,    4.5,    1.0)),
    Kart(15, "Wario Car", 2, 6,
        KartStats(142.0,    122.0,    74.0,    20.0,    0.15,    0.005,    10.0,    2.50,    5.0,    1.0)),
    Kart(16, "DK Jumbo", 2, 1,
        KartStats(143.0,    123.0,    71.0,    20.0,    0.10,    0.005,    10.0,    2.75,    5.0,    0.9)),
    Kart(17, "Koopa King", 2, 7,
        KartStats(144.0,    124.0,    68.0,    20.0,    0.08,    0.005,    10.0,    3.00,    5.0,    0.9)),
    Kart(18, "Piranha Pipes", 2, 19,
        KartStats(143.0,    123.0,    86.0,    20.0,    0.10,    0.005,    10.0,    3.00,    5.0,    0.9)),
    Kart(19, "Boo Pipes", 2, 18,
        KartStats(137.0,    117.0,    92.0,    20.0,    2.00,    0.010,    10.0,    3.00,    5.0,    0.9)),
    Kart(20, "Parade Kart", -1, 20,
        KartStats(142.0,    122.0,    74.0,    20.0,    0.30,    0.005,    30.0,    2.50,    5.0,    1.0)),
]

NORMAL_CUPS = [
    "Mushroom Cup",
    "Flower Cup",
    "Star Cup",
    "Special Cup",
]
CUPS = NORMAL_CUPS + ["All Cup Tour"]
CUP_ALL_CUP_TOUR = 4

class CourseType(IntEnum):
    RACE = 0
    BATTLE = 1
    CEREMONY = 2
    MENU = 3

class Course(NamedTuple):
    name: str = ""
    id: int = -1
    type: CourseType = CourseType.RACE
    staff_time: float = 0
    good_time: float = 0
    owners: list[int] = []
    laps: int = 3
    ghost_characters: list[int] = []
    ghost_kart: int = -1
    music: int = -1
    """Low byte of the course BGM sound id (0x2000000 | music). Final lap variant is music + 0x10."""


# Staff ghost combos (ghost_characters, ghost_kart) are read from the StaffGhosts/*.ght file headers.
RACE_COURSES = [
    # Race courses:
    Course("Luigi Circuit",     0x24, staff_time =  86.277, good_time = 95, owners = [1], ghost_characters = [1, 0], ghost_kart = 8, music = 0x03),
    Course("Peach Beach",       0x22, staff_time =  80.404, good_time = 90, owners = [2], ghost_characters = [2, 3], ghost_kart = 10, music = 0x01),
    Course("Baby Park",         0x21, staff_time =  71.108, good_time = 80, owners = [6, 7], laps = 7, ghost_characters = [6, 7], ghost_kart = 0, music = 0x00),
    Course("Dry Dry Desert",    0x32, staff_time = 110.755, good_time = 120, ghost_characters = [5, 4], ghost_kart = 12, music = 0x0e),
    Course("Mushroom Bridge",   0x28, staff_time =  91.458, good_time = 100, ghost_characters = [10, 11], ghost_kart = 2, music = 0x06),
    Course("Mario Circuit",     0x25, staff_time = 101.384, good_time = 115, owners = [0], ghost_characters = [0, 1], ghost_kart = 8, music = 0x04),
    Course("Daisy Cruiser",     0x23, staff_time = 112.207, good_time = 125, owners = [3], ghost_characters = [3, 2], ghost_kart = 10, music = 0x02),
    Course("Waluigi Stadium",   0x2a, staff_time = 119.658, good_time = 130, owners = [17], ghost_characters = [17, 16], ghost_kart = 15, music = 0x08),
    Course("Sherbet Land",      0x33, staff_time =  85.904, good_time = 100, ghost_characters = [7, 6], ghost_kart = 0, music = 0x0f),
    Course("Mushroom City",     0x29, staff_time = 110.663, good_time = 120, ghost_characters = [11, 10], ghost_kart = 2, music = 0x07),
    Course("Yoshi Circuit",     0x26, staff_time = 119.886, good_time = 135, owners = [4], ghost_characters = [4, 5], ghost_kart = 12, music = 0x05),
    Course("DK Mountain",       0x2d, staff_time = 132.639, good_time = 145, owners = [12], ghost_characters = [12, 13], ghost_kart = 16, music = 0x0b),
    Course("Wario Colosseum",   0x2b, staff_time = 141.106, good_time = 155, owners = [16], laps = 2, ghost_characters = [16, 17], ghost_kart = 15, music = 0x09),
    Course("Dino Dino Jungle",  0x2c, staff_time = 120.908, good_time = 140, ghost_characters = [13, 12], ghost_kart = 16, music = 0x0a),
    Course("Bowser's Castle",   0x2f, staff_time = 164.690, good_time = 185, owners = [14], ghost_characters = [14, 15], ghost_kart = 17, music = 0x0c),
    Course("Rainbow Road",      0x31, staff_time = 196.476, good_time = 210, ghost_characters = [0, 2], ghost_kart = 8, music = 0x0d),
]

COURSES = RACE_COURSES + [
    Course("Cookie Land", 0x3a, CourseType.BATTLE),
    Course("Pipe Plaza", 0x3b, CourseType.BATTLE),
    Course("Block City", 0x36, CourseType.BATTLE),
    Course("Nintendo Gamecube", 0x35, CourseType.BATTLE),
    Course("Luigi's Mansion", 0x34, CourseType.BATTLE),
    Course("Tilt-A-Kart", 0x38, CourseType.BATTLE),
    
    Course("Award Ceremony", 0x44, CourseType.CEREMONY),
    Course("Menu", 0, CourseType.MENU),
]


class Modes(IntEnum):
    TIMETRIAL = 1
    GRANDPRIX = 2
    VERSUS = 3
    BATTLE_BALLOON = 4
    BATTLE_ROBBERY = 5
    BATTLE_SHINE = 7
    BATTLE_BOMB = 6
    CEREMONY = 8

UNSUPPORTED_MODES = [Modes.VERSUS, Modes.BATTLE_BALLOON, Modes.BATTLE_ROBBERY, Modes.BATTLE_SHINE, Modes.BATTLE_BOMB]


def ensure_cups_courses_per_class(cups_courses: list) -> list[list[list[int]]]:
    """Expands course arrangements from slot data to the per vehicle class format.
    Slot data from before course shuffle per class holds a single arrangement."""
    if len(cups_courses) > 0 and len(cups_courses[0]) > 0 and isinstance(cups_courses[0][0], int):
        return [[list(cup) for cup in cups_courses] for _ in range(4)]
    return cups_courses

class Item(NamedTuple):
    id: int
    name: str
    short_name: str
    usefulness: int = 0
    weight_table: list[int] = []
    guaranteed_position: int = 0
    is_boost_item: bool = False
    no_first_place: bool = False

    def get_weight(self, rank: int, frantic: int) -> int:
        if self.no_first_place and rank == 0:
            return 0
        return int((self.weight_table[rank] * (100 - frantic) + 100 * frantic) / 100)

    def is_guaranteened(self, rank: int, frantic: int) -> bool:
        if self.no_first_place and rank == 0:
            return False
        return rank >= round(self.guaranteed_position * (1 - frantic / 100))

ITEMS = [
    Item(0, "Green Shell", "GrSh",          2, [ 90,  50,  25,  10,   0,   0,   0,   0], 0),
    Item(1, "Bowser's Shell", "BoSh",       3, [ 30,  60, 100, 100, 100,  90,  40,   0], 2),
    Item(2, "Red Shell", "ReSh",            3, [ 10,  55,  70,  70,  70,  50,  40,  20], 2),
    Item(3, "Banana", "Ba",                 1, [ 70,  35,  15,   5,   0,   0,   0,   0], 0),
    Item(4, "Giant Banana", "GBa",          2, [120, 100,  90,  60,  30,   0,   0,   0], 0),
    Item(5, "Mushroom", "Mu",               4, [  0,  40,  65,  75,  65,  35,  10,  10], 3, is_boost_item=True),
    Item(6, "Star", "St",                   5, [  0,   0,   0,  10,  20,  30,  40,  40], 6, is_boost_item=True),
    Item(7, "Chain Chomp", "CC",            4, [  0,   0,   0,   3,  20,  60, 130, 180], 6),
    Item(8, "Bob-omb", "Bo",                1, [ 10,  70, 100, 100, 100,  90,  40,   0], 1),
    Item(10, "Lightning", "Li",             3, [  0,   0,   0,   0,   3,  10,  20,  30], 7),
    Item(11, "Yoshi Egg", "Eg",             4, [ 50,  70,  80,  80,  80,  70,  60,  40], 1),
    Item(12, "Golden Mushroom", "GMu",      6, [  0,   3,  10,  30,  50,  80, 100, 120], 5, is_boost_item=True),
    Item(13, "Spiny Shell", "SpSh",         0, [  0,   0,   5,  10,  10,  20,  20,  20], 6, no_first_place=True),
    Item(14, "Heart", "He",                 4, [  0,   0,   3,  10,  30,  90, 110, 130], 5),
    Item(15, "Fake Item", "FI",             0, [ 30,  20,  10,   0,   0,   0,   0,   0], 0),
    Item(17, "Triple Green Shells", "3GS",  3, [ 20,  50, 100, 100, 100,  90,  40,   0], 2),
    Item(18, "Triple Mushrooms", "3Mu",     6, [  0,   0,  10,  20,  35,  50,  70,  90], 5, is_boost_item=True),
    Item(19, "Triple Red Shells", "3RS",    4, [  5,  40,  60,  70,  70,  50,  50,  30], 3),
    Item(21, "Fireballs", "Fi",             2, [ 30,  70, 100, 100, 100,  90,  40,   0], 1),
    Item(20, "None", "",                    0, [  0,   0,   0,   0,   0,   0,   0,   0], 8),
]

ITEM_GREEN_SHELL = ITEMS[0]
ITEM_BOWSER_SHELL = ITEMS[1]
ITEM_RED_SHELL = ITEMS[2]
ITEM_BANANA = ITEMS[3]
ITEM_GIANT_BANANA = ITEMS[4]
ITEM_MUSHROOM = ITEMS[5]
ITEM_STAR = ITEMS[6]
ITEM_CHAIN_CHOMP = ITEMS[7]
ITEM_BOBOMB = ITEMS[8]
ITEM_LIGHTNING = ITEMS[9]
ITEM_YOSHI_EGG = ITEMS[10]
ITEM_GOLDEN_MUSHROOM = ITEMS[11]
ITEM_SPINY_SHELL = ITEMS[12]
ITEM_HEART = ITEMS[13]
ITEM_FAKE_ITEM = ITEMS[14]
ITEM_TRIPLE_GREEN_SHELLS = ITEMS[15]
ITEM_TRIPLE_MUSHROOMS = ITEMS[16]
ITEM_TRIPLE_RED_SHELLS = ITEMS[17]
ITEM_FIREBALLS = ITEMS[18]
ITEM_NONE = ITEMS[19]

TT_ITEM_TABLE = [
    bytes([ITEM_NONE.id, ITEM_MUSHROOM.id]),
    bytes([ITEM_MUSHROOM.id, ITEM_MUSHROOM.id]),
    bytes([ITEM_NONE.id, ITEM_TRIPLE_MUSHROOMS.id]),
    bytes([ITEM_STAR.id, ITEM_TRIPLE_MUSHROOMS.id]),
]


class ItemHit(NamedTuple):
    """An item the player can hit an opponent with (item hit locations)."""
    name: str
    """Item name with an article, used in the location name."""
    items: list[Item]
    """Item unlocks that make this hit possible."""
    kinds: list[int]
    """Item kinds of the hitting item object as reported by the game."""

# Items that cause a crash with attribution to the item's owner. Not every item
# qualifies: star and lightning hits carry no item object in the crash code.
ITEM_HITS = [
    ItemHit("a Green Shell", [ITEM_GREEN_SHELL, ITEM_TRIPLE_GREEN_SHELLS], [0, 17]),
    ItemHit("a Red Shell", [ITEM_RED_SHELL, ITEM_TRIPLE_RED_SHELLS], [2, 19]),
    ItemHit("Bowser's Shell", [ITEM_BOWSER_SHELL], [1]),
    ItemHit("a Banana", [ITEM_BANANA], [3]),
    ItemHit("a Giant Banana", [ITEM_GIANT_BANANA], [4]),
    ItemHit("a Bob-omb", [ITEM_BOBOMB], [8]),
    ItemHit("a Spiny Shell", [ITEM_SPINY_SHELL], [13]),
    ItemHit("a Yoshi Egg", [ITEM_YOSHI_EGG], [11]),
    ItemHit("a Fireball", [ITEM_FIREBALLS], [21, 9]),
    ItemHit("Chain Chomp", [ITEM_CHAIN_CHOMP], [7]),
]


class Obstacle(NamedTuple):
    """A course obstacle that can be defeated (obstacle locations)."""
    name: str
    """Obstacle name with an article, used in the location name."""
    obj_id: int
    """Course object id (from the BOL object data)."""
    courses: list[str]
    """Names of the courses the obstacle appears on."""

# Item kinds that defeat obstacles. Taken from the goomba's item hit check,
# the same set is assumed for the other obstacles until tested.
OBSTACLE_WEAPON_KINDS = [0, 1, 2, 7, 8, 9, 11, 13, 17, 19, 21]
OBSTACLE_STAR_CAUSE = 0xfe
"""Cause byte for running an obstacle over with a star."""

OBSTACLES = [
    Obstacle("a Goomba", 0x0e7f, ["Mario Circuit"]),
    Obstacle("a Piranha Plant", 0x0e80, ["Mario Circuit", "Yoshi Circuit"]),
    Obstacle("a Chain Chomp", 0x0e78, ["Luigi Circuit", "Mario Circuit"]),
    Obstacle("a Cataquack", 0x0d4a, ["Peach Beach"]),
    Obstacle("a Pokey", 0x1389, ["Dry Dry Desert"]),
    Obstacle("a Shy Guy", 0x13ee, ["Sherbet Land"]),
]


class KartUpgrade(NamedTuple):
    id: int
    name: str
    short_name: str
    usefulness: int

KART_UPGRADES = [
    KartUpgrade(0, "Acceleration Boost", "ACC", 10),
    KartUpgrade(1, "Mini-turbo Extender", "TUR", 10),
    KartUpgrade(2, "Off-road Tires", "OFR", 8),
    KartUpgrade(3, "Extra Weight", "WEI", 2),
    KartUpgrade(4, "Power Steering", "STE", 8),
]

KART_UPGRADE_ACC = KART_UPGRADES[0]
KART_UPGRADE_TURBO = KART_UPGRADES[1]
KART_UPGRADE_OFFROAD = KART_UPGRADES[2]
KART_UPGRADE_WEIGHT = KART_UPGRADES[3]
KART_UPGRADE_STEER = KART_UPGRADES[4]

ENGINE_UPGRADE_USEFULNESS = 50
SKIP_DIFFICULTY_USEFULNESS = 200
