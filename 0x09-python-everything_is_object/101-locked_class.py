#!/usr/bin/python3
"""This depicts blocked class moduel"""


class LockedClass:
    """This object prevents dynamic attribute"""

    __slots__ = ['first_name']
