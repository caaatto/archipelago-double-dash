"""
Tests that the correct locations are generated depending on options.
"""
from . import MkddTestBase
from worlds.mario_kart_double_dash import locations as mkdd_locs, items as mkdd_items, game_data


def _location_names(test_base) -> set:
    return {loc.name for loc in test_base.multiworld.get_locations(test_base.player)}


BASE_OPTIONS = {
    "goal": "trophies",
    "trophy_requirement": 0,
    "grand_prix_trophies": False,
    "shuffle_extra_trophies": 0,
    "kart_upgrades": 0,
    "items_for_everybody": 0,
    "items_per_character": 0,
    "start_items_per_character": 0,
    "item_boxes_as_locations": "disabled",
}


class TestTTLocationsDisabled(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "disable"}

    def test_no_good_time_locations(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertNotIn(mkdd_locs.get_loc_name_good_time(course), location_names)

    def test_no_staff_ghost_locations(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertNotIn(mkdd_locs.get_loc_name_ghost(course.name), location_names)


class TestTTLocationsBasic(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "basic"}

    def test_all_good_time_locations_exist(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertIn(mkdd_locs.get_loc_name_good_time(course), location_names)

    def test_no_staff_ghost_locations(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertNotIn(mkdd_locs.get_loc_name_ghost(course.name), location_names)


class TestTTLocationsStaffGhosts(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "include_staff_ghosts"}

    def test_all_good_time_locations_exist(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertIn(mkdd_locs.get_loc_name_good_time(course), location_names)

    def test_all_staff_ghost_locations_exist(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertIn(mkdd_locs.get_loc_name_ghost(course.name), location_names)


class TestGrandPrixTrophyLocations(MkddTestBase):
    options = {**BASE_OPTIONS, "grand_prix_trophies": True, "time_trials": "disable"}

    def test_all_trophy_locations_exist(self) -> None:
        location_names = _location_names(self)
        for cup in game_data.NORMAL_CUPS:
            for vehicle_class in range(4):
                name = mkdd_locs.get_loc_name_trophy(cup, vehicle_class)
                self.assertIn(name, location_names)


class TestNoGrandPrixTrophyLocations(MkddTestBase):
    options = {**BASE_OPTIONS, "grand_prix_trophies": False, "time_trials": "disable"}

    def test_no_trophy_locations(self) -> None:
        location_names = _location_names(self)
        for cup in game_data.NORMAL_CUPS:
            for vehicle_class in range(4):
                name = mkdd_locs.get_loc_name_trophy(cup, vehicle_class)
                self.assertNotIn(name, location_names)


class TestAllCupTourGoalLocation(MkddTestBase):
    options = {**BASE_OPTIONS, "goal": "all_cup_tour", "time_trials": "disable"}

    def test_win_all_cup_tour_location_exists(self) -> None:
        location_names = _location_names(self)
        self.assertIn(mkdd_locs.WIN_ALL_CUP_TOUR, location_names)


class TestTrophiesGoalNoAllCupTourLocation(MkddTestBase):
    options = {**BASE_OPTIONS, "goal": "trophies", "time_trials": "disable"}

    def test_win_all_cup_tour_location_absent(self) -> None:
        location_names = _location_names(self)
        self.assertNotIn(mkdd_locs.WIN_ALL_CUP_TOUR, location_names)


class TestCupLocationsAlwaysPresent(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "disable"}

    def test_all_cup_finish_locations_exist(self) -> None:
        location_names = _location_names(self)
        for cup in game_data.NORMAL_CUPS:
            self.assertIn(mkdd_locs.get_loc_name_finish(cup), location_names)

    def test_all_cup_gold_50cc_locations_exist(self) -> None:
        location_names = _location_names(self)
        for cup in game_data.NORMAL_CUPS:
            self.assertIn(mkdd_locs.get_loc_name_cup(cup, 0, 0), location_names)


class TestGhostComboLocations(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "disable"}

    def test_all_ghost_combo_locations_exist(self) -> None:
        location_names = _location_names(self)
        for course in game_data.RACE_COURSES:
            self.assertIn(mkdd_locs.get_loc_name_win_ghost_combo(course), location_names)

    def test_ghost_combo_data_is_complete(self) -> None:
        for course in game_data.RACE_COURSES:
            self.assertEqual(len(course.ghost_characters), 2)
            self.assertIn(course.ghost_kart, range(len(game_data.KARTS)))


class TestCustomTimeTrialTimes(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "basic",
               "custom_time_trial_times": {"Luigi Circuit": [95, 87, 90.5]}}

    def test_only_defined_time_locations_exist(self) -> None:
        location_names = _location_names(self)
        for i in range(3):
            self.assertIn(mkdd_locs.get_loc_name_custom_time("Luigi Circuit", i), location_names)
        for i in range(3, 5):
            self.assertNotIn(mkdd_locs.get_loc_name_custom_time("Luigi Circuit", i), location_names)
        self.assertNotIn(mkdd_locs.get_loc_name_custom_time("Peach Beach", 0), location_names)

    def test_times_are_sorted_easiest_first(self) -> None:
        times = self.world.options.custom_time_trial_times.value["Luigi Circuit"]
        self.assertEqual(times, sorted(times, reverse = True))


class TestCustomTimeTrialTimesDisabled(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "disable",
               "custom_time_trial_times": {"Luigi Circuit": [95]}}

    def test_no_time_locations_without_time_trials(self) -> None:
        location_names = _location_names(self)
        self.assertNotIn(mkdd_locs.get_loc_name_custom_time("Luigi Circuit", 0), location_names)


class TestItemHitLocations(MkddTestBase):
    # Note: no item unlocks configured, so the pool ensure mechanism has to kick in.
    options = {**BASE_OPTIONS, "time_trials": "disable"}

    def test_all_item_hit_locations_exist(self) -> None:
        location_names = _location_names(self)
        for hit in game_data.ITEM_HITS:
            self.assertIn(mkdd_locs.get_loc_name_item_hit(hit), location_names)
        self.assertIn(mkdd_locs.HIT_YOURSELF, location_names)

    def test_hit_item_unlocks_are_in_the_pool(self) -> None:
        pool_names = {item.name for item in self.multiworld.itempool}
        for hit in game_data.ITEM_HITS:
            unlock_names = []
            for item in hit.items:
                unlock_names.append(mkdd_items.get_item_name_character_item(None, item.name))
                unlock_names.extend(
                    mkdd_items.get_item_name_character_item(character.name, item.name)
                    for character in game_data.CHARACTERS)
            self.assertTrue(any(name in pool_names for name in unlock_names),
                            f"No unlock enabling '{hit.name}' hits in the pool")


class TestItemHitLocationsDisabled(MkddTestBase):
    options = {**BASE_OPTIONS, "time_trials": "disable", "item_hits_as_locations": False}

    def test_no_item_hit_locations(self) -> None:
        location_names = _location_names(self)
        for hit in game_data.ITEM_HITS:
            self.assertNotIn(mkdd_locs.get_loc_name_item_hit(hit), location_names)
        self.assertNotIn(mkdd_locs.HIT_YOURSELF, location_names)
