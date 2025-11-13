#!/usr/bin/env python3

from src.voting import *

def print_results(tally: dict):
    """Output the results of the election, with the average votes for each candidate."""
    winner = determine_winner(tally)

    print("\nResults\n")

    for candidate in tally:
        print(f"{candidate}: {tally[candidate]}")

    print(f"{winner} wins with the average score {tally[winner]}!\n")

print_results(tally_candidates(get_votes()))
