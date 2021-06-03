#!/usr/bin/python3
"""class Student module"""


class Student():
    """student class"""

    def __init__(self, first_name, last_name, age):
        """"Init the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary"""
        if type(attrs) == list:
            json_dict = {}
            nwdict = self.__dict__
            for attr in attrs:
                if type(attr) != str:
                    return self.__dict__
                if attr in nwdict:
                    json_dict.setdefault(attr, self.__dict__[attr])
            return json_dict
        return self.__dict__

    def reload_from_json(self, json):
        """change all attributes"""
        for p, r in json.items():
            self.__dict__[p] = r
