#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = 0
    newlist = []
    for i in range(list_length):
        try:
            div = float(my_list_1[i]) / float(my_list_2[i])
            newlist.append(div)
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        except ValueError:
            print("wrong type")
            newlist.append(0)
        except IndexError:
            print("out of range")
            newlist.append(0)
    return (newlist)
