#!/usr/bin/python3
""" class to print list """


class MyList(list):
    """ class to print list """

    def __init__(self):
        """ function  __init__  """
        super().__init__(self)

    def print_sorted(self):
        """ function print_sorted """
        print(sorted(self))
