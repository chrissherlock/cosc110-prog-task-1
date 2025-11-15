#!/usr/bin/env python3

from src.voting import *
from src.voting_io import *


def main() -> None:
    """
    Voting program for COSC110

    This program takes a single vote from each voter (represented as a 7-digit
    number) for a list of three candidates. The vote value is from 0 to 9, the
    program then tallies an average for each candidate, outputs the results and
    pronounces the winner.

    Programming notes:

    When researching how to organise Python projects, I learned about how
    to setup Python modules so I have created a basic module under the src
    directory. A sticking point was how to test the module as it generated
    module errors, but after some more research I learned about relative
    imports which resolved the issue.
    """

    print_results(tally_candidates(get_votes()))


if __name__ == "__main__":
    main()
