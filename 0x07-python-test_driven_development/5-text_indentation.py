#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """
       Prints indent text
    """

    if type(text) != str or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    ver = 0
    for i in text:
        if i == '?' or i == ':' or i == '.':
            print(i, end="\n\n")
            ver = 1
        else:
            if ver == 0:
                print(i, end="")
            else:
                if i == ' ' or i == '\t':
                    pass
                else:
                    print(i, end="")
                    ver = 0
