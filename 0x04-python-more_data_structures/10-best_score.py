#!/usr/bin/python3
def best_score(a_dictionary):
    return (max(a_dictionary.items(), key=lambda n: n[1])[0] if a_dictionary else None)
