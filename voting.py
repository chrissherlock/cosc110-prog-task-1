#!/usr/bin/env python3


def main() -> None:
    """
    Voting program for COSC110

    This program takes a single vote from each voter (represented as a 7-digit
    number) for a list of three candidates. The vote value is from 0 to 9, the
    program then tallies an average for each candidate, outputs the results and
    pronounces the winner.
    """

    print_results(tally_candidates(get_votes()))


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

    return 0 if len(votes) == 0 else sum(votes) / len(votes)


def tally_candidates(candidates: dict[str, list]) -> dict[str, int]:
    """
    Get the tally of all the votes for the candidates and determine the winner.

    Args:
        candidates(dict): the candidates and their list of votes

    Returns:
        A tally of all the candidates average votes.

    """

    return {candidate: get_candidate_average_votes(votes) for candidate, votes in candidates.items()}


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


def is_valid_voterid(voter_id: str) -> bool:
    """
    Checks the voter id is 7 numeric digits.

    Args:
        voter_id(str): The voter ID to be validated.

    Returns:
        True if the voter id is valid, False if the voter id is invalid
    """

    # preconditions
    try:
        voter_id_int = int(voter_id)
    except ValueError:
        return False
    else:
        return (
            len(voter_id) == 7 and voter_id_int >= 1000000 and voter_id_int <= 9999999
        )


def is_valid_vote(vote: str) -> bool:
    """
    Checks the vote is between 0 and 9.

    Args:
        vote(str): vote preference value for the candidate

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


def has_already_voted(voters: list[str], voterid: str) -> bool:
    """
    Checks if the voter has already voted.

    Args:
        voters(list): list of voters who have already voted.

    Raises:
        ValueError: if not a valid voterid

    Returns:
        True if the voter has already voted, False if the voter has
        not voted.
    """

    # preconditions
    if not is_valid_voterid(str(voterid)):
        raise ValueError(f"voter id is not valid: {voterid}")

    return voterid in voters


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

        if not is_valid_voterid(str(voterid)):
            print("Invalid Voter ID\n")
            continue

        if has_already_voted(voters, voterid):
            print("You have already voted in this election. You cannot vote again.\n")
            continue

        voters.append(voterid)

        for candidate in candidates:
            vote_pref = input(prompt_text_for_candidate(candidate))

            while not is_valid_vote(str(vote_pref)):
                print("Please enter an integer score between 0 and 9")
                vote_pref = input(prompt_text_for_candidate(candidate))

            candidates[candidate].append(int(vote_pref))

    return candidates


def format_number(num: float) -> str:
    """
    Take a floating point number and format it to the correct decimal precision.

    Rules:
    - if the number is a whole number, then add a .0 on the end (e.g. 1 => 1.0)
    - if the number has one decimal place then keep to one decimal place (e.g. 1.1 => 1.1)
    - if the number has more than two decimal places, then round to two decimal places
      (e.g. 1.333 => 1.33)

    Args:
        num(float): number to be converted to the resulting string

    Returns:
        String conforming to the rules above
    """
    if num % 1 == 0:  # no decimal place
        return f"{num:.1f}"

    return f"{num:.3g}"


def print_results(tally: dict[str, int]) -> None:
    """
    Output the results of the election, with the average votes for each candidate.

    Args:
        tally(dict): each of the candidates average votes.
    """

    print("\nResults\n")

    for candidate, votes in tally.items():
        print(f"{candidate}: {format_number(votes)}")

    winner = determine_winner(tally)

    print(f"{winner} wins with the average score {format_number(tally[winner])}!\n")


if __name__ == "__main__":
    main()
