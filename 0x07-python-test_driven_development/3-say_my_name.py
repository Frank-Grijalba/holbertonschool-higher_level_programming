#!/usr/bin/python3
"""
    >>> tester.say_my_name("John", "Smith")
    My name is John Smith

"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError('first_name must be a string')
    print("My name is " + first_name + " " + last_name)
