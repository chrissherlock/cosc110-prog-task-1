#!/usr/bin/env python3

import unittest
from src.verify import is_integer

class TestVerifications(unittest.TestCase):
    """Test suite for verifications module"""

    def test_is_integer(self):
        """Test the is_integer function."""
        self.assertTrue(is_integer(1111))
        self.assertFalse(is_integer(1.111))
        self.assertFalse(is_integer("abcd"))

if __name__ == '__main__':
    unittest.main()
