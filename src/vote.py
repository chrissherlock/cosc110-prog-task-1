#!/usr/bin/env python3

from verify import *

# ask for a voter id until a blank is entered

voterid = input("Please enter Voter ID: ")

while voterid != "":
    if not is_valid_voterid(voterid):
        print("Invalid Voter ID\n")

    voterid = input("Please enter Voter ID: ")
