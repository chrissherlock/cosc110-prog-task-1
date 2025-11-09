#!/usr/bin/env python3

import sys
import os
import unittest

from src.voting import *

class TestVerifications(unittest.TestCase):
    """Test suite for voting module"""

    def test_has_aleady_voted(self):
        """test to see if the voter has already voted"""
        voters = ["1111111", "1234567"]

        self.assertTrue(has_already_voted(voters, "1234567"))
        self.assertFalse(has_already_voted(voters, "7654321"))

if __name__ == '__main__':
    unittest.main()
