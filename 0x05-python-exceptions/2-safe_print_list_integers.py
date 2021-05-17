#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            int(my_list[i])
            print("{}".format(my_list[i]), end="")
            j += 1
        except ValueError:
            continue
        except TypeError:
            continue
        # except IndexError:
    print("")
    return j
