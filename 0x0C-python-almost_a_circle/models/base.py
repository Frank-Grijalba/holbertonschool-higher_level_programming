#!/usr/bin/python3
""" Base """
import json
from os import path


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        x = json.dumps(list_dictionaries)
        return x

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        js = ""
        lst_obj = []
        if list_objs is None or len(list_objs) == 0:
            with open(cls.__name__ + ".json", mode="w") as f:
                f.write("[]")
                return
        for i in list_objs:
            dic = i.to_dictionary()
            lst_obj.append(dic)
        js += i.to_json_string(lst_obj)
        with open(cls.__name__ + ".json", mode='w') as f:
            f.write(js)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        "Load json string from json file"
        if not path.isfile(cls.__name__ + ".json"):
            return []
        ls = []
        with open(cls.__name__ + ".json", 'r') as f:
            t = f.read()
            t = cls.from_json_string(t)
        for i in t:
            dummy = cls.create(**i)
            ls.append(dummy)
        return ls
