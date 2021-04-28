#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        j = 0
    else:
        j = 1
    print("{:s}".format(chr(i - (32 * j))), end="")
