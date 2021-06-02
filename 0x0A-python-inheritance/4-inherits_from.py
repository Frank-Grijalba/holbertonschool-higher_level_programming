#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Return if the object is an instance that is inherited"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
