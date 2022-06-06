#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    witout modifying the original list

    Args:
        my_list: list of integers
        idx: integers
        element: integers

    Return:
        list of intergers
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list[:]

    return my_list[:idx] + [element] + my_list[idx + 1:]
