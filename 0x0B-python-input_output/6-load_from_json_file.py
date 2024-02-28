#!/usr/bin/python3
"""JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, mode='r') as f:
        obj = json.load(f)
        return obj
