#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Return if the object is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
