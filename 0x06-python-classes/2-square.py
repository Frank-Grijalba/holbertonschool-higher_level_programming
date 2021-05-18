#!/usr/bin/python3
"""2-square
a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """a class Square"""
    def __init__(self, size=0):
        """Square class init, assign a value to
        Args:
            size (int): The private arg size of the square.
        Raises:
            ValueError: If size is less than Zero
            TypeError: If size is not an integer
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
