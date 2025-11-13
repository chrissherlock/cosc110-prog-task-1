#!/usr/bin/env python3

from .verify import *

def has_already_voted(voters: list, voterid: str) -> bool:
    """
    Checks that the value entered is an integer.

    Args:
        voters(list): list of voters who have already voted.

    Preconditions:
        - voters parameter is a list
        - voterid parameter is a string
        - the voterid is valid

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

def prompt_text_for_candidate(candidate: str) -> str:
    """
    Generates the prompt to rate a candidate.

    Args:
        candidate(str): name of the candidate to be rated

    Preconditions:
        - candidate parameter is a string

    Returns:
        Prompt string with the candidate name.
    """

    # preconditions
    try:
        if not isinstance(candidate, str):
            raise TypeError("candidate is not a string")
    except TypeError as e:
        print(f"The type exception is: {str(e)}")

    return f"Please enter an integer score for {candidate} (0 is worst, 9 is best): "
    
def get_candidate_average_votes(votes: list) -> float:
    """
    Gets the average votes for a candidate.

    Args:
        votes(list): list of votes for a particular candidate

    Preconditions:
        - votes must be a list
        - the list must contain only integers

    Returns:
        Average vote for the candidate.
    """

    # preconditions
    try:
        if not isinstance(votes, list):
            raise TypeError("votes is not a list")
        # use a generator expression to check the type of each element in the list
        if not all(isinstance(vote, int) for vote in votes):
            raise TypeError("all the votes must be an integer")
    except TypeError as e:
        print(f"The type exception is: {str(e)}")

    if len(votes) == 0:
        return 0

    return sum(votes) / len(votes)

def determine_winner(tally: dict) -> str:
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

    Preconditions:
        - the tally must be a dictionary

    Returns:
        The election winner.
    """

    # preconditions
    try:
        if not isinstance(tally, dict):
            raise TypeError("tally is not a dict")
    except TypeError as e:
        print(f"The type exception is: {str(e)}")

    if tally["William Gorithm"] >= tally["Meg A. Byte"] and tally["William Gorithm"] >= tally["Oliver Seton"]:
        return "William Gorithm"

    if tally["Meg A. Byte"] >= tally["Oliver Seton"]:
        return "Meg A. Byte"

    return "Oliver Seton"

def get_votes() -> dict:
    """
    Ask for a voter id until a blank is entered.

    Returns:
        A dictionary of candidates and their list of votes.
    """

    voters = []

    candidates = {
        "William Gorithm": [],
        "Meg A. Byte": [],
        "Oliver Seton": []
    }

    while True:
        voterid = input("Please enter Voter ID: ")

        if voterid == '':
            break

        if not is_valid_voterid(voterid):
            print("Invalid Voter ID\n")
            continue;

        if has_already_voted(voters, voterid):
            print("You have already voted in this election. You cannot vote again.\n")
            continue;
            
        voters.append(voterid)

        for candidate in candidates:
            vote_pref = input(prompt_text_for_candidate(candidate))

            while not is_valid_vote(vote_pref):
                print("Please enter an integer score between 0 and 9")
                vote_pref = input(prompt_text_for_candidate(candidate))

            candidates[candidate].append(int(vote_pref))

    return candidates

def tally_candidates(candidates: dict) -> dict:
    """
    Get the tally of all the votes for the candidates and determine the winner.

    Args:    
        candidates(dict): the candidates and their list of votes
        
    Returns:
        A tally of all the candidates average votes.

    """

    # preconditions
    try:
        if not isinstance(candidates, dict):
            raise TypeError("candidates is not a dict")
    except TypeError as e:
        print(f"The type exception is: {str(e)}")

    tally = {}

    for candidate in candidates:
        tally[candidate] = get_candidate_average_votes(candidates[candidate])

    return tally

def print_results(tally: dict):
    """
    Output the results of the election, with the average votes for each candidate.

    Args:
        tally(dict): each of the candidates average votes.

    """
    # preconditions
    try:
        if not isinstance(tally, dict):
            raise TypeError("tally is not a dict")
    except TypeError as e:
        print(f"The type exception is: {str(e)}")

    winner = determine_winner(tally)

    print("\nResults\n")

    for candidate in tally:
        print(f"{candidate}: {tally[candidate]}")

    print(f"{winner} wins with the average score {tally[winner]}!\n")
