#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sort_key = sorted(a_dictionary.keys())
        for key in sort_key:
            print("{}: {}".format(key, a_dictionary[key]))
