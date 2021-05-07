#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        return (max(a_dictionary.items(), key=lambda n: n[1])[0])
    else:
        return None
