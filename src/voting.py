#!/usr/bin/env python3

from .verify import *

def has_already_voted(voters: list, voterid: int) -> bool:
    """checks that the value entered is an integer"""

    # preconditions
    assert isinstance(voters, list)
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
