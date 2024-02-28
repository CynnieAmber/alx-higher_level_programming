#!/usr/bin/python3
""" File writing function """


def append_write(filename="", text=""):
    """ function to write file contents """
    with open(filename, mode='a', encoding='utf-8') as myfile:
        return myfile.write(text)
