#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys_to_del = [k for k, v in a_dictionary.items() if value == v]
        for k in keys_to_del:
            del a_dictionary[k]
        return a_dictionary
