#!/usr/bin/env python3

def is_valid_voterid(voter_id) -> bool:
    """checks the voter id is 7 numeric digits"""
    return voter_id.isdigit() and int(voter_id) >= 1000000 and int(voter_id) <= 9999999

def is_valid_vote(vote) -> bool:
    """checks the vote is between 0 and 9"""
    return vote.isdigit() and int(vote) >= 0 and int(vote) <= 9
