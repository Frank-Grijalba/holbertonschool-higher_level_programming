#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """Area not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is a int or bigger than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
