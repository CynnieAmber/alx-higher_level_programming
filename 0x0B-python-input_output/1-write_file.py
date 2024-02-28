#!/usr/bin/python3
""" File writing function """


def write_file(filename="", text=""):
    """ function to write file contents """
    with open(filename, mode='w', encoding='utf-8') as myfile:
        return myfile.write(text)
