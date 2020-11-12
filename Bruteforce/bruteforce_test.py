from hashlib import sha256 as hash_f
import unittest
from Bruteforce.bruteforce import bruteforce


def sha256(string):
    return hash_f(string.encode('utf-8'))


class TestBruteforce(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_alphabet(self):
        self.assertEqual(bruteforce(sha256("hello"), "", 1), "")

    def test_zero_length_password(self):
        self.assertEqual(bruteforce(sha256("hello"), "abc", 0), "")

    def test_password_max_length_1(self):
        self.assertEqual(bruteforce(sha256("b"), "abc", 1), "b")
        self.assertEqual(bruteforce(sha256("d"), "abc", 1), "")

    def test_password_max_length_2(self):
        self.assertEqual(bruteforce(sha256("ab"), "abc", 2), "ab")
        self.assertEqual(bruteforce(sha256("c"), "abc", 2), "c")
        self.assertEqual(bruteforce(sha256("d"), "abc", 2), "")

    def test_password_max_length_3(self):
        self.assertEqual(bruteforce(sha256("bac"), "abc", 3), "bac")
        self.assertEqual(bruteforce(sha256("ba"), "abc", 3), "ba")
        self.assertEqual(bruteforce(sha256("aba"), "abc", 3), "aba")
        self.assertEqual(bruteforce(sha256("a"), "abc", 3), "a")
        self.assertEqual(bruteforce(sha256("bad"), "abc", 3), "")

    def test_missing_symbols_in_alphabet(self):
        self.assertEqual(bruteforce(sha256("daddy"), "abc", 3), "")
        self.assertEqual(bruteforce(sha256("$#!"), "abc", 3), "")

    def test_max_length_is_too_small(self):
        self.assertEqual(bruteforce(sha256("baca"), "abc", 3), "")
        self.assertEqual(bruteforce(sha256("cba"), "abc", 2), "")

    def test_small_alphabet(self):
        self.assertEqual(bruteforce(sha256("ddd"), "d", 4), "ddd")
        self.assertEqual(bruteforce(sha256("dcd"), "d", 3), "")


if __name__ == "__main__":
    unittest.main()
