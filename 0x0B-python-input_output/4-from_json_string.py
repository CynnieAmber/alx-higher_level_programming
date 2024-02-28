#!/usr/bin/python3
""" json function """
import json


def from_json_string(my_str):
    """ function to deserialize to string """
    return json.loads(my_str)
