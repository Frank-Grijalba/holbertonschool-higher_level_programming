#!/usr/bin/python3
"""3-rectangle a class Rectangle that defines
   a rectangle by: (based on 2-rectangle.py)
"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """"Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * self.__height) * 2

    def __str__(self):
        """str"""
        str = ''
        if self.__width == 0 or self.__height == 0:
            return ()
        for i in range(self.__height):
            str = str + ("#" * self.__width) + '\n'
        return (str[:-1])
