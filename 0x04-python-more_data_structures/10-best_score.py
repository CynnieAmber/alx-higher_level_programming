#!/usr/bin/python3
def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def best_score(a_dictionary):
    if a_dictionary:
        len_val = len(a_dictionary.keys())
        if len_val > 0:
            sort_val = 0
            lst_score = []
            for key, value in a_dictionary.items():
                lst_score.append(value)
            lst_score.sort()
            key = find_key_by_value(a_dictionary, lst_score[len_val - 1])
            return key
        else:
            return None
    else:
        return None
