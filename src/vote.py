#!/usr/bin/env python3

from verify import *

voterid = input("Please enter Voter ID: ")
if not is_valid_voterid(voterid):
    print("Invalid Voter ID\n")
