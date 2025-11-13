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

def has_already_voted(voters: list, voterid: str) -> bool:
    """
    Checks if the voter has already voted.

    Args:
        voters(list): list of voters who have already voted.

    Raises:
        TypeError: if voters is not a list or the voterid is not a string
        ValueError: if not a valid voterid

    Returns:
        True if the voter has already voted, False if the voter has
        not voted.
    """

    # preconditions
    try:
        if not isinstance(voters, list):
            raise TypeError("voters parameter is not a list")
        if not isinstance(voterid, str):
            raise TypeError("voterid parameter is not a list")
        if not is_valid_voterid(voterid):
            raise ValueError(f"voter id is not valid: {voterid}")
    except TypeError as e:
        print(f"The type exception is: {str(e)}")
    except ValueError as e:
        print(f"The value exception is {str(e)}")

    return voterid in voters
