#!/usr/bin/python3


def safe_print_integer(value):
    """Prints integers
    Args:
    The integers to be printed.
    Return:
    True if printed.
    False if not.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
