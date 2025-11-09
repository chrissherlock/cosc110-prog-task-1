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

if __name__ == '__main__':
    unittest.main()
