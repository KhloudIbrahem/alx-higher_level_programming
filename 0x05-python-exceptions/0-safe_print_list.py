#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints the elements in the list
    Args:
    my_list (list): The list to be printed.
    x (int): The number of elements to be printed.
    Return:
    The number of printed elements.
    """
    i = 0
    printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            break
    print("")
    return (printed)
