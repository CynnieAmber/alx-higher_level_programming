#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common_elements = set()
    # common_elements = set_1.intersection(set_2)
    # common_elements = set_1 && set_2
    common_elements = set_1 ^ set_2
    return common_elements
