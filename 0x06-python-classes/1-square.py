#!/usr/bin/python3
"""1-square
a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """a class Square"""
    def __init__(self, size):
        """Square class init, assign a value to
        Args:
            size (int): The private arg size of the square.
        """
        self.__size = size
