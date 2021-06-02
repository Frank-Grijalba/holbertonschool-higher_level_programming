#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """Init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area"""
        return self.__size ** 2

    def __str__(self):
        """str method"""
        return("[Square] " + str(self.__size) + "/" + str(self.__size))
