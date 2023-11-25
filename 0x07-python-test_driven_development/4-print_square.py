#!/usr/bin/python3
"""Define printing square function"""


def print_square(size):
    """Implements the print square function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
