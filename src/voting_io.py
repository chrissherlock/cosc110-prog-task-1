#!/usr/bin/env python3

from .validate import *
from .voting import *


def prompt_text_for_candidate(candidate: str) -> str:
    """
    Generates the prompt to rate a candidate.

    Args:
        candidate(str): name of the candidate to be rated

    Raises:
        TypeError: if candidate parameter is not a string

    Returns:
        Prompt string with the candidate name.
    """

    # preconditions
    if not isinstance(candidate, str):
        raise TypeError("candidate is not a string")

    return f"Please enter an integer score for {candidate} (0 is worst, 9 is best): "


def get_votes() -> dict[str, list]:
    """
    Ask for a voter id until a blank is entered.

    Returns:
        A dictionary of candidates and their list of votes.
    """

    voters: list[str] = []

    candidates: dict[str, list] = {
        "William Gorithm": [],
        "Meg A. Byte": [],
        "Oliver Seton": [],
    }

    while True:
        voterid = input("Please enter Voter ID: ")

        if voterid == "":
            break

        if not is_valid_voterid(voterid):
            print("Invalid Voter ID\n")
            continue

        if has_already_voted(voters, voterid):
            print("You have already voted in this election. You cannot vote again.\n")
            continue

        voters.append(voterid)

        for candidate in candidates:
            vote_pref = input(prompt_text_for_candidate(candidate))

            while not is_valid_vote(vote_pref):
                print("Please enter an integer score between 0 and 9")
                vote_pref = input(prompt_text_for_candidate(candidate))

            candidates[candidate].append(int(vote_pref))

    return candidates


def print_results(tally: dict[str, int]) -> None:
    """
    Output the results of the election, with the average votes for each candidate.

    Args:
        tally(dict): each of the candidates average votes.

    Raises:
        TypeError: if tally is not a dict
    """
    # preconditions
    if not isinstance(tally, dict):
        raise TypeError("tally is not a dict")

    print("\nResults\n")

    for candidate in tally:
        print(f"{candidate}: {tally[candidate]}")

    winner = determine_winner(tally)

    print(f"{winner} wins with the average score {tally[winner]}!\n")
