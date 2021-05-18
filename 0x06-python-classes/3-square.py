#!/usr/bin/python3
"""3-square
a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """a class Square"""
    def __init__(self, size=0):
        """Square class init, assign a value to
        Args:
            size (int): The private arg size of the square.
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Method to calc the area of a square.
        Returns: 
            The area of a square.
        """
        return self.__size ** 2
