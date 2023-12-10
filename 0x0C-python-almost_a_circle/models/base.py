#!/usr/bin/python3
"""Define the Base class"""


class Base:
    """Represent the base class
    Attributes:
        private class attribute:
            __nb_objects (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor to initialize the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
