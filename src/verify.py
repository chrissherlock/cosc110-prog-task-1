#!/usr/bin/env python3

def is_integer(value) -> bool:
    """checks that the value entered is an integer"""
    return isinstance(value, (int))

def is_valid_voterid(voter_id) -> bool:
    """checks the voter id is 7 numeric digits"""
    return is_integer(voter_id) and voter_id >= 1000000 and voter_id <= 9999999
