#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boo = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            boo.append(True)
        else:
            boo.append(False)

    return (boo)
