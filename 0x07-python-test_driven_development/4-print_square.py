#!/usr/bin/python3
""" ....... """


def print_square(size):
    """ square printing """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
                for i in range(size):
                    for j in range(size):
                        print("#", end="")
                    print()
