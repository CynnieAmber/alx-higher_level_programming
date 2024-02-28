#!/usr/bin/python3
"""json dictionary representation of an object"""


def class_to_json(obj):
    """ function to return dict attributes """
    return obj.__dict__
