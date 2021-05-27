#!/usr/bin/python3
"""
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Print a square
    """
    str = ""
    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        str = str + ("#" * size) + "\n"
    print(str[:-1])
