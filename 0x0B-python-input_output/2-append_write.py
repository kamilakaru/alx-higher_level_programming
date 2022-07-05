#!/usr/bin/python3
"""defining append_write with two arguments"""


def append_write(filename="", text=""):
    """append filename with utf-8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
