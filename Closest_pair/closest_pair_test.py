from Closest_pair.closest_pair import closest_pair, Point, make_pair
import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_points(self):
        self.assertEqual("Exception", closest_pair([]))

    def test_single_point(self):
        self.assertEqual("Exception", closest_pair([Point(1, 1)]))

    def test_two_points(self):
        self.assertEqual(closest_pair([Point(2, 3), Point(3, 4)]), make_pair(Point(2, 3), Point(3, 4)))

    def test_three_points(self):
        self.assertEqual(closest_pair([Point(2, 3), Point(1, 9), Point(6, 2)]), make_pair(Point(2, 3), Point(6, 2)))

    def test_duplicate_points(self):
        self.assertEqual(closest_pair([Point(2, 3), Point(2, 3), Point(3, 4)]), make_pair(Point(2, 3), Point(2, 3)))

    def test_same_x_coordinate(self):
        self.assertEqual(closest_pair([Point(2, 9), Point(2, 4), Point(2, 1), Point(2, -8)]), make_pair(Point(2, 1), Point(2, 4)))

    def test_many_points(self):
        self.assertEqual(closest_pair([
            Point(2, 3), Point(0, 4), Point(11, 9), Point(2, 8),
            Point(4, 4), Point(3, 6), Point(6, 5), Point(1, 9)]), make_pair(Point(1, 9), Point(2, 8)))

    def test_negative_points(self):
        self.assertEqual(closest_pair([
            Point(-5, 6), Point(1, 2), Point(4, -2), Point(-9, 0),
            Point(-1, -2), Point(0, 7), Point(2, -1), Point(-3, 1)]), make_pair(Point(2, -1), Point(4, -2)))

    def test_closest_points_are_from_stripe(self):
        self.assertEqual(closest_pair([
            Point(-1, 20), Point(-1.5, 10), Point(-2, -10), Point(-2.7, -20),
            Point(-10, 20), Point(-10.5, 10), Point(-11.7, -10), Point(-12.2, -20),
            Point(1, 21), Point(1.5, 11), Point(2, -9), Point(2.7, -19),
            Point(10, 21), Point(10.5, 11), Point(11.7, -9), Point(12.2, -19)]), make_pair(Point(-1, 20), Point(1, 21)))


if __name__ == "__main__":
    unittest.main()
