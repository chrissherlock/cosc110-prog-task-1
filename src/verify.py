#!/usr/bin/env python3

def is_valid_voterid(voter_id) -> bool:
    """checks the voter id is 7 numeric digits"""
    return voter_id.isdigit() and int(voter_id) >= 1000000 and int(voter_id) <= 9999999
