#!/usr/bin/env python3

from src.verify import *
from src.voting import *

# ask for a voter id until a blank is entered

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

    for key in candidates:
        vote_pref = input(prompt_text_for_candidate(key))

        while not is_valid_vote(vote_pref):
            print("Please enter an integer score between 0 and 9")
            vote_pref = input(prompt_text_for_candidate(key))

        candidates[key].append(vote_pref)
