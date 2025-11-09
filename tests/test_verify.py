#!/usr/bin/env python3

import unittest
from src.verify import is_valid_voterid

class TestVerifications(unittest.TestCase):
    """Test suite for verifications module"""

    def test_is_valid_voterid(self):
        """Test to ensure voter ID is a 7-digit integer"""
        self.assertTrue(is_valid_voterid("1000000"))
        self.assertTrue(is_valid_voterid("5555555"))
        self.assertTrue(is_valid_voterid("9999999"))

        # 6 digit integer
        self.assertFalse(is_valid_voterid("999999"))

        # negative 7 digit integer
        self.assertFalse(is_valid_voterid("-9999999"))

        # not an integer
        self.assertFalse(is_valid_voterid("abcde"))

    def test_is_valid_vote(self):
        """Test to ensure the vote is between 0 and 9"""
        self.assertTrue(is_valid_vote("0")
        self.assertTrue(is_valid_vote("1")
        self.assertTrue(is_valid_vote("2")
        self.assertTrue(is_valid_vote("3")
        self.assertTrue(is_valid_vote("4")
        self.assertTrue(is_valid_vote("5")
        self.assertTrue(is_valid_vote("6")
        self.assertTrue(is_valid_vote("7")
        self.assertTrue(is_valid_vote("8")
        self.assertTrue(is_valid_vote("9")

        self.assertFalse(is_valid_vote("xyz")
        self.assertFalse(is_valid_vote("10")
        self.assertFalse(is_valid_vote("")

if __name__ == '__main__':
    unittest.main()
