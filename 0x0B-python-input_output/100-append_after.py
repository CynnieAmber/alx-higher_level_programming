#!/usr/bin/python3
""" append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Function to append text after the search string in a file """
    with open(filename, 'r') as file:
        lines = file.readlines()

    str = ""
    for i in range(len(lines)):
        str += lines[i]
        if search_string in lines[i]:
            str += new_string

    with open(filename, 'w') as file:
        file.write(str)
