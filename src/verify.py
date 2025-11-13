#!/usr/bin/env python3


def is_valid_voterid(voter_id: str) -> bool:
    """
    Checks the voter id is 7 numeric digits.

    Args:
        voter_id(str): The voter ID to be validated.

    Raises:
        ValueError: if voter_id is not an integer

    Returns:
        True if the voter id is valid, False if the voter id is invalid
    """

    # preconditions
    try:
        voter_id_int = int(voter_id)
    except ValueError:
        return False
    else:
        return voter_id_int >= 1000000 and voter_id_int <= 9999999


def is_valid_vote(vote: str) -> bool:
    """
    Checks the vote is between 0 and 9.

    Args:
        vote(str): vote preference value for the candidate

    Raises:
        ValueError: if vote parameter is not a number

    Returns:
        True if the vote pref is valid, False if the vote pref is invalid
    """

    # preconditions
    try:
        vote_int = int(vote)
    except ValueError:
        return False
    else:
        return vote_int >= 0 and vote_int <= 9
