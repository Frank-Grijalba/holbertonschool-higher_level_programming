#!/usr/bin/python3
"""
>>> add_integer(2, 3)
5

"""


def add_integer(a, b=98):
    """
    Add two integers
    """
    if type(a) not in [float, int]:
            raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
            raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
