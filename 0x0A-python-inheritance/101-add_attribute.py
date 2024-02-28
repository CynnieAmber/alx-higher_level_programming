#!/usr/bin/python3
""" add_attribute module """


def add_attribute(obj, attr_name, attr_value):
    """ add attribute to an object """
    if hasattr(obj, "__dict__"):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
