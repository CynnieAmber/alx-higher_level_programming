#!/usr/bin/python3
""" File reading function """


def read_file(filename=""):
    """ function to read file contents """
    with open(filename, mode='r', encoding='utf-8') as myfile:
        data = myfile.read()
        print(data, end="")
