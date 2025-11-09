#!/usr/bin/env python3

import sys
import os
import unittest

from src.voting import *

class TestVoting(unittest.TestCase):
    """Test suite for voting module"""

    def test_has_aleady_voted(self):
        """test to see if the voter has already voted"""
        voters = ["1111111", "1234567"]

        self.assertTrue(has_already_voted(voters, "1234567"))
        self.assertFalse(has_already_voted(voters, "7654321"))

    def test_prompt_text_for_candidate(self):
        """test to ensure that candidate prompt is correct"""
        self.assertEqual("Please enter an integer score for William Gorithm (0 is worst, 9 is best): ", prompt_text_for_candidate("William Gorithm"))

if __name__ == '__main__':
    unittest.main()
