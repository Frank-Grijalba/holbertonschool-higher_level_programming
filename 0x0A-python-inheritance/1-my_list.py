#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
