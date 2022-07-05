#!/usr/bin/python3
"""
contains inherits_from function
"""


def inherits_from(obj, a_class):
    """True if obj is a subclass of a_class, otherwise False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
