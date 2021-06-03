#!/usr/bin/python3
"""class Student module"""


class Student():
    """student class"""

    def __init__(self, first_name, last_name, age):
        """"Init the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary"""
        return self.__dict__
