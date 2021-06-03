#!/usr/bin/python3
"""Write a file"""


def write_file(filename="", text=""):
    """Write a file"""
    with open(filename, mode="w", encoding='utf-8') as f:
        return(f.write(text))
