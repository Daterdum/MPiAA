from Count_sort.count_sort import count_sort
import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_array(self):
        self.assertEqual(count_sort([], 0, 0), [])

    def test_one_element_array(self):
        self.assertEqual(count_sort([1], 1, 1), [1])

    def test_array_from_one_element(self):
        self.assertEqual(count_sort([1, 1, 1, 1], 1, 1), [1, 1, 1, 1])

    def test_sorted_array(self):
        self.assertEqual(count_sort([1, 2, 4, 9], 1, 9), [1, 2, 4, 9])

    def test_unsorted_array(self):
        self.assertEqual(count_sort([3, 0, -1, 9, 2], -1, 9), [-1, 0, 2, 3, 9])

    def test_sorted_array_with_duplicates(self):
        self.assertEqual(count_sort([0, 1, 1, 2, 2, 2, 9], 0, 10), [0, 1, 1, 2, 2, 2, 9])

    def test_unsorted_array_with_duplicates(self):
        self.assertEqual(count_sort([9, -1, 2, 1, -1, 3, 9, 2], -10, 10), [-1, -1, 1, 2, 2, 3, 9, 9])

    def test_array_with_big_range(self):
        self.assertEqual(count_sort([1, 0, 1000000, 0, -1000000], -2000000, 2000000), [-1000000, 0, 0, 1, 1000000])


if __name__ == "__main__":
    unittest.main()
