#!/usr/bin/python3
""" int rebel """


class MyInt(int):
    """ int rebel """

    def __eq__(self, other):
        """ int inverted equals """
        return super().__ne__(other)

    def __ne__(self, other):
        """ int inverted not equals """
        return super().__eq__(other)
