#!/usr/bin/python3
j = 0
for i in range(10):
    for j in range(i + 1, 10):
        if i < 9 and j < 9:
            print("{:d}{:d}".format(i, j), end=", ")
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
