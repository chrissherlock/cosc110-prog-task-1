#!/usr/bin/env python3

def is_valid_voterid(voter_id: str) -> bool:
    """
    Checks the voter id is 7 numeric digits.

    Args:
        voter_id(str): The voter ID to be validated.

    Preconditions:
        - voter_id parameter is a string

    Returns:
        True if the voter id is valid, False if the voter id is invalid
    """

    # preconditions
    assert(isinstance(voter_id, str))

    return voter_id.isdigit() and int(voter_id) >= 1000000 and int(voter_id) <= 9999999

def is_valid_vote(vote: str) -> bool:
    """
    Checks the vote is between 0 and 9.

    Args:
        vote(str): vote preference value for the candidate

    Preconditions:
        - vote parameter is a string

    Returns:
        True if the vote pref is valid, False if the vote pref is invalid
    """

    # preconditions
    assert(isinstance(vote, str))

    return vote.isdigit() and int(vote) >= 0 and int(vote) <= 9
