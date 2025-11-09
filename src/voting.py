#!/usr/bin/env python3

from .verify import *

def has_already_voted(voters: list, voterid: str) -> bool:
    """checks that the value entered is an integer"""

    # preconditions
    assert isinstance(voters, list)
    assert isinstance(voterid, str)
    assert is_valid_voterid(voterid), f"voter id is not valid: {voterid}"

    return voterid in voters

def prompt_text_for_candidate(candidate: str) -> str:
    return f"Please enter an integer score for {candidate} (0 is worst, 9 is best): "
    
def get_candidate_average_votes(votes: list) -> float:
    """gets the average votes for a candidate"""

    # preconditions
    assert len(votes) > 0

    # all the votes must be an integer - here I use a generator expression to
    # check the type of each element in the list
    assert all(isinstance(vote, int) for vote in votes)

    return sum(votes) / len(votes)

def determine_winner(tally: dict) -> str:
    """algorithm determines the winner

    If there is a tie, the candidate listed first in the above order wins:

    * William Gorithm wins whenever no candidate has a higher score than him
      (i.e., even if others have the same score).
    * If William Gorithm has a lower score than any other candidate, and the
      other candidates are tied, then Meg A. Byte wins.
    * Oliver Seton only wins if he has a higher score than the other
      candidates."""

    if tally["William Gorithm"] >= tally["Meg A. Byte"] and tally["William Gorithm"] >= tally["Oliver Seton"]:
        return "William Gorithm"

    if tally["Meg A. Byte"] >= tally["Oliver Seton"]:
        return "Meg A. Byte"

    return "Oliver Seton"
