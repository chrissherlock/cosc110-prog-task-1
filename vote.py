#!/usr/bin/env python3

from src.verify import *
from src.voting import *

# ask for a voter id until a blank is entered

voters = []
voterid = input("Please enter Voter ID: ")

while voterid != "":
    if not is_valid_voterid(voterid):
        print("\nInvalid Voter ID\n")

    if has_already_voted(voters, voterid):
        print("\nYou have already voted in this election. You cannot vote again.\n")
        
    voters.append(voterid)

    voterid = input("Please enter Voter ID: ")
