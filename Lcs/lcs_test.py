from Lcs.lcs import lcs
import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        pass

    def test_both_strings_are_empty(self):
        self.assertEqual(lcs("", ""), "")

    def test_one_string_is_empty(self):
        self.assertEqual(lcs("", "abcd"), "")
        self.assertEqual(lcs("abcd", ""), "")

    def test_equal_strings(self):
        self.assertEqual(lcs("abcd", "abcd"), "abcd")

    def test_substring(self):
        self.assertEqual(lcs("abab", "ab"), "ab")

    def test_substring_in_the_middle(self):
        self.assertEqual(lcs("xyaban", "abarab"), "aba")

    def test_subsequences(self):
        self.assertEqual(lcs("nahybser", "iunkayxbis"), "naybs")
        self.assertEqual(lcs("z1artunx", "yz21rx"), "z1rx")
        self.assertEqual(lcs("z1arxzyx1a", "yz21rx"), "z1rx")
        self.assertEqual(lcs("yillnum", "numyjiljil"), "yill")

    def test_reverse_subsequence(self):
        result = lcs("xablar", "ralbax")
        self.assertIn(result, ("aba", "ala"))


if __name__ == "__main__":
    unittest.main()
