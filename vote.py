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

voterid = input("Please enter Voter ID: ")

while voterid != "":
    if not is_valid_voterid(voterid):
        print("Invalid Voter ID\n")

    if has_already_voted(voters, voterid):
        print("You have already voted in this election. You cannot vote again.\n")
        
    voters.append(voterid)

    voterid = input("Please enter Voter ID: ")
