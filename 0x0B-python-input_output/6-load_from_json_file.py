#!/usr/bin/python3

"""creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """Create an Object"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
