#!/usr/bin/env python3

from src.voting import *

tally = tally_candidates(get_votes())
winner = determine_winner(tally)

# output the results of the election, with the average votes for each candidate,
# and the name of the actual winner

print("\nResults\n")

for candidate in tally:
    print(f"{candidate}: {tally[candidate]}")

print(f"{winner} wins with the average score {tally[winner]}!\n")
