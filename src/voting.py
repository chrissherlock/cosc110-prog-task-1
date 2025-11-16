#!/usr/bin/env python3

from .validate import *


def get_candidate_average_votes(votes: list) -> float:
    """
    Gets the average votes for a candidate.

    Args:
        votes(list): list of votes for a particular candidate

    Raises:
        TypeError: if the list contain non-integers

    Returns:
        Average vote for the candidate.
    """

    # preconditions
    # use a generator expression to check the type of each element in the list
    if not all(isinstance(vote, int) for vote in votes):
        raise TypeError("all the votes must be an integer")

    if len(votes) == 0:
        return 0

    return sum(votes) / len(votes)


def tally_candidates(candidates: dict[str, list]) -> dict[str, int]:
    """
    Get the tally of all the votes for the candidates and determine the winner.

    Args:
        candidates(dict): the candidates and their list of votes

    Returns:
        A tally of all the candidates average votes.

    """

    tally: dict[str, int] = {}

    for candidate in candidates:
        tally[candidate] = get_candidate_average_votes(candidates[candidate])

    return tally


def determine_winner(tally: dict[str, int]) -> str:
    """
    Algorithm that determines the winner.

    Those with the largest average votes wins.

    If there is a tie, the candidate listed first in the above order wins:

    * William Gorithm wins whenever no candidate has a higher score than him
      (i.e., even if others have the same score).
    * If William Gorithm has a lower score than any other candidate, and the
      other candidates are tied, then Meg A. Byte wins.
    * Oliver Seton only wins if he has a higher score than the other
      candidates.

    Args:
        tally(dict): dictionary of each candidate with their average total vote

    Returns:
        The election winner.
    """

    if (
        tally["William Gorithm"] >= tally["Meg A. Byte"]
        and tally["William Gorithm"] >= tally["Oliver Seton"]
    ):
        return "William Gorithm"

    if tally["Meg A. Byte"] >= tally["Oliver Seton"]:
        return "Meg A. Byte"

    return "Oliver Seton"
