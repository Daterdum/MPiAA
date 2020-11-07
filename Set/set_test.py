from Set.set import Set
import unittest


class TestSet(unittest.TestCase):
    def setUp(self):
        s = Set()

    def test_empty_set(self):
        s = Set()
        self.assertEqual(s.size(), 0)
        self.assertFalse(s.find(1))

    def test_one_item(self):
        s = Set()
        s.insert(1)
        self.assertEqual(s.size(), 1)
        self.assertTrue(s.find(1))

    def test_several_items(self):
        s = Set()
        s.insert(2)
        s.insert(1)
        s.insert(3)
        self.assertEqual(s.size(), 3)
        self.assertTrue(s.find(2))
        self.assertTrue(s.find(1))
        self.assertTrue(s.find(3))
        self.assertFalse(s.find(0))

    def test_duplicate_items(self):
        s = Set()
        s.insert(2)
        s.insert(2)
        s.insert(3)
        self.assertEqual(s.size(), 2)
        self.assertTrue(s.find(2))
        self.assertTrue(s.find(3))
        self.assertFalse(s.find(1))

    def test_many_items(self):
        s = Set()
        s.insert(5)
        s.insert(3)
        s.insert(6)
        s.insert(4)
        s.insert(3)
        s.insert(2)
        self.assertEqual(s.size(), 5)
        self.assertTrue(s.find(5))
        self.assertTrue(s.find(3))
        self.assertTrue(s.find(2))
        self.assertFalse(s.find(10))

    def test_negative_items(self):
        s = Set()
        s.insert(0)
        s.insert(-2)
        s.insert(-1)
        s.insert(-2)
        s.insert(1)
        self.assertEqual(s.size(), 4)
        self.assertTrue(s.find(-1))
        self.assertTrue(s.find(1))
        self.assertTrue(s.find(-2))
        self.assertFalse(s.find(2))


if __name__ == "__main__":
    unittest.main()
