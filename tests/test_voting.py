#!/usr/bin/env python3

import unittest

from src.voting import *
from src.voting_io import prompt_text_for_candidate


class TestVoting(unittest.TestCase):
    """Test suite for voting module"""

    def test_prompt_text_for_candidate(self):
        """test to ensure that candidate prompt is correct"""
        self.assertEqual(
            "Please enter an integer score for William Gorithm (0 is worst, 9 is best): ",
            prompt_text_for_candidate("William Gorithm"),
        )

        # check preconditions
        with self.assertRaises(TypeError):
            prompt_text_for_candidate(111)

    def test_get_candidate_average_vote(self):
        """test to get the candidates average vote"""
        candidate_votes = [1, 3, 5, 7]
        self.assertEqual(4, get_candidate_average_votes(candidate_votes))

        # check preconditions
        with self.assertRaises(TypeError):
            get_candidate_average_votes("not a list")

        with self.assertRaises(TypeError):
            get_candidate_average_votes(["not an integer"])

    def test_tally_candidates(self):
        """ensure the tally is correct"""
        tally = {"William Gorithm": [1, 2, 3]}
        self.assertEqual(2, tally_candidates(tally)["William Gorithm"])

        novotes_tally = {"William Gorithm": [0, 0]}
        self.assertEqual(0, tally_candidates(novotes_tally)["William Gorithm"])

        # check preconditions
        with self.assertRaises(TypeError):
            tally_candidates("not a list")

    def test_determine_winner(self):
        """test that winner is determined correctly"""

        tally_clear_winner = {
            "William Gorithm": 1.5,
            "Meg A. Byte": 5.5,
            "Oliver Seton": 4.5,
        }

        self.assertEqual(
            "Meg A. Byte",
            determine_winner(tally_clear_winner),
            msg="Meg A. Byte should be the winner with 5.5",
        )

        tally_william_tied = {
            "William Gorithm": 5.5,
            "Meg A. Byte": 4.5,
            "Oliver Seton": 5.5,
        }

        self.assertEqual(
            "William Gorithm",
            determine_winner(tally_william_tied),
            msg="William Gorithm tied with Oliver Seton",
        )

        tally_meg_tied = {
            "William Gorithm": 4.5,
            "Meg A. Byte": 5.5,
            "Oliver Seton": 5.5,
        }

        self.assertEqual(
            "Meg A. Byte",
            determine_winner(tally_meg_tied),
            msg="William Gorith tied with Meg A. Byte",
        )

        tally_clear_winner_oliver = {
            "William Gorithm": 1.5,
            "Meg A. Byte": 1.5,
            "Oliver Seton": 4.5,
        }

        self.assertEqual("Oliver Seton", determine_winner(tally_clear_winner_oliver))

        tally_all_stinkers = {"William Gorithm": 0, "Meg A. Byte": 0, "Oliver Seton": 0}

        self.assertEqual(
            "William Gorithm",
            determine_winner(tally_all_stinkers),
            msg="William Gorith should be the winner when everyone gets 0 votes",
        )

        # check preconditions
        with self.assertRaises(TypeError):
            determine_winner("not a list")

if __name__ == "__main__":
    unittest.main()
