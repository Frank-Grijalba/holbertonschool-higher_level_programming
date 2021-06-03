#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read())
