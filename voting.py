#!/usr/bin/env python3

from src.verify import *
from src.voting import *

def get_votes() -> dict:
    """Ask for a voter id until a blank is entered."""
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
    """Get the tally of all the votes for the candidates and determine the winner"""
    tally = {}

    for candidate in candidates:
        tally[candidate] = get_candidate_average_votes(candidates[candidate])

    return tally

tally = tally_candidates(get_votes())
winner = determine_winner(tally)

# output the results of the election, with the average votes for each candidate,
# and the name of the actual winner

print("\nResults\n")

for candidate in tally:
    print(f"{candidate}: {tally[candidate]}")

print(f"{winner} wins with the average score {tally[winner]}!\n")
