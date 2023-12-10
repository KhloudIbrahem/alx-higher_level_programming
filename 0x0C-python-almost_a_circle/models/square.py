#!/usr/bin/python3
"""Define the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square attributes
        Args:
        size (int): the size length.
        x (int): the coordinate x.
        y (int): the coordinate y.
        id (int): the identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve it"""
        return self.width

    @size.setter
    def size(self, value):
        """set it"""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)


