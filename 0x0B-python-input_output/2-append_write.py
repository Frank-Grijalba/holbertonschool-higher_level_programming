#!/usr/bin/python3
"""To append write in a file"""


def append_write(filename="", text=""):
    """Append text in a file"""
    with open(filename, mode="a", encoding='utf-8') as f:
        return(f.write(text))
