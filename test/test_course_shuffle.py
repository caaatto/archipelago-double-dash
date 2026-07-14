"""
Tests for course shuffle logic.
"""
from . import MkddTestBase
from worlds.mario_kart_double_dash import game_data


class TestCourseShuffleVanilla(MkddTestBase):
    options = {"course_shuffle": "vanilla"}

    def test_four_classes_with_four_cups_each_with_four_courses(self) -> None:
        self.assertEqual(len(self.world.cups_courses), 4)
        for arrangement in self.world.cups_courses:
            self.assertEqual(len(arrangement), 4)
            for courses in arrangement:
                self.assertEqual(len(courses), 4)

    def test_vanilla_order_preserved(self) -> None:
        for arrangement in self.world.cups_courses:
            for cup_id, courses in enumerate(arrangement):
                expected = list(range(cup_id * 4, cup_id * 4 + 4))
                self.assertEqual(courses, expected)

    def test_all_sixteen_courses_present(self) -> None:
        for arrangement in self.world.cups_courses:
            all_courses = [c for cup in arrangement for c in cup]
            self.assertEqual(sorted(all_courses), list(range(16)))


class TestCourseShuffleOnce(MkddTestBase):
    options = {"course_shuffle": "shuffle_once"}

    def test_four_classes_with_four_cups_each_with_four_courses(self) -> None:
        self.assertEqual(len(self.world.cups_courses), 4)
        for arrangement in self.world.cups_courses:
            self.assertEqual(len(arrangement), 4)
            for courses in arrangement:
                self.assertEqual(len(courses), 4)

    def test_all_classes_share_the_same_arrangement(self) -> None:
        for arrangement in self.world.cups_courses:
            self.assertEqual(arrangement, self.world.cups_courses[0])

    def test_all_sixteen_courses_present_exactly_once(self) -> None:
        all_courses = [c for cup in self.world.cups_courses[0] for c in cup]
        self.assertEqual(len(all_courses), 16)
        self.assertEqual(len(set(all_courses)), 16) # Checks no courses appear more than once

    def test_all_course_indices_valid(self) -> None:
        all_courses = [c for cup in self.world.cups_courses[0] for c in cup]
        for course_id in all_courses:
            self.assertIn(course_id, range(16))

    def test_courses_reference_valid_race_courses(self) -> None:
        for cup_id, courses in enumerate(self.world.cups_courses[0]):
            for course_id in courses:
                course = game_data.RACE_COURSES[course_id]
                self.assertIsNotNone(course.name)


class TestCourseShufflePerClass(MkddTestBase):
    options = {"course_shuffle": "shuffle_per_class"}

    def test_four_classes_with_four_cups_each_with_four_courses(self) -> None:
        self.assertEqual(len(self.world.cups_courses), 4)
        for arrangement in self.world.cups_courses:
            self.assertEqual(len(arrangement), 4)
            for courses in arrangement:
                self.assertEqual(len(courses), 4)

    def test_all_sixteen_courses_present_exactly_once_per_class(self) -> None:
        for arrangement in self.world.cups_courses:
            all_courses = [c for cup in arrangement for c in cup]
            self.assertEqual(sorted(all_courses), list(range(16)))

    def test_cup_exits_cover_all_classes(self) -> None:
        for cup_name, course_classes in self.world.cup_course_classes.items():
            cup_no = game_data.CUPS.index(cup_name)
            for vehicle_class in range(4):
                for course_id in self.world.cups_courses[vehicle_class][cup_no]:
                    self.assertIn(course_id, course_classes)
                    self.assertIn(vehicle_class, course_classes[course_id])


class TestCupsCoursesSlotDataCompatibility(MkddTestBase):
    def test_old_format_is_expanded(self) -> None:
        old_format = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        expanded = game_data.ensure_cups_courses_per_class(old_format)
        self.assertEqual(len(expanded), 4)
        for arrangement in expanded:
            self.assertEqual(arrangement, old_format)

    def test_new_format_is_unchanged(self) -> None:
        new_format = [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]] * 4
        self.assertEqual(game_data.ensure_cups_courses_per_class(new_format), new_format)
