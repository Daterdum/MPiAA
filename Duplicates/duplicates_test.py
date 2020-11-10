from Duplicates.duplicates import has_duplicates, get_duplicates_2
import unittest


class TestDuplicates(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_array(self):
        data = []
        self.assertFalse(has_duplicates(data))
        self.assertEqual(sorted(get_duplicates_2(data)), [])

    def test_single_element(self):
        data = [1]
        self.assertFalse(has_duplicates(data))
        self.assertEqual(sorted(get_duplicates_2(data)), [])

    def test_many_elements(self):
        data = [2, 1, -4, 7]
        self.assertFalse(has_duplicates(data))
        self.assertFalse(sorted(get_duplicates_2(data)), [])

    def test_many_elements_one_duplicate(self):
        data = [2, -3, 0, 2, 7, 1]
        self.assertTrue(has_duplicates(data))
        self.assertEqual(sorted(get_duplicates_2(data)), [2])

    def test_many_elements_many_duplicates(self):
        data = [2, -3, 0, 2, 1, -3, 4, 1, -1, 2]
        self.assertTrue(has_duplicates(data))
        self.assertEqual(sorted(get_duplicates_2(data)), [-3, 1, 2])

    def test_single_duplicated_elem(self):
        data = [4, 4, 4, 4]
        self.assertTrue(has_duplicates(data))
        self.assertEqual(sorted(get_duplicates_2(data)), [4])


if __name__ == "__main__":
    unittest.main()
