#!/usr/bin/python3
"""1-rectangle a class Rectangle that defines
a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """class rectangle"""

    def __init__(self, width=0, height=0):
        """Rectangle class init, assign a value to
        Args:
            width (int): The private arg width of the Rectangle.
            height (int): The private arg height of the Rectangle.
        Raise:
            ValueError: If value is less than Zero
            TypeError: If value is not an integer
        """
        if width < 0 or height < 0:
            raise ValueError("size must be >= 0")
        if type(width) is not int or type(height) is not int:
            raise TypeError("size must be an integer")

        self.__width = width
        self.__height = height


@property
def width(self):
    """Method getter.
        Returns:
            The size of a triangle.
        """
    return self.__width


@width.setter
def width(self, value):
    """Method setter: set the width
        Args:
            value (int): set into width of the triangle.
        Raise:
            ValueError: If value is less than Zero
            TypeError: If value is not an integer
        """
    if type(value) is not int:
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value


@property
def height(self):
    """Method getter.
        Returns:
            The height of a triangle.
        """
    return self.__height


@height.setter
def height(self, value):
    """Method setter: set the height
        Args:
            value (int): set into height of the triangle.
        Raise:
            ValueError: If value is less than Zero
            TypeError: If value is not an integer
        """
    if type(value) is not int:
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__height = height
