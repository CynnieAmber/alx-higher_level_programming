#!/usr/bin/python3
"""JSON file-reading function."""
import json
import sys


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, mode='r') as f:
        obj = json.load(f)
        return obj


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)


# Load existing data from file, if it exists
try:
    data = load_from_json_file('add_item.json')
except FileNotFoundError:
    data = []
# Add command-line arguments to the data list
data.extend(sys.argv[1:])
# Save the updated data list to the file
save_to_json_file(data, 'add_item.json')
