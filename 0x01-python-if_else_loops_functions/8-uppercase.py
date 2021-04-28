#!/usr/bin/env python3
def uppercase(str):
    string = ""
    for i in range(len(str)):
        asc_ii = ord(str[i])
        if asc_ii >= 97 and asc_ii < 123:
            string = string + chr(asc_ii - 32)
        else:
            string = string + chr(asc_ii)
    print("{:s}".format(string))
