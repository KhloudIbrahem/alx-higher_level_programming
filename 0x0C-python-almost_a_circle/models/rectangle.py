#!/usr/bin/python3
"""Define the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent the Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attributes of the rectangle
        Args:
        width (int): the width.
        height (int): the height.
        x (int): the x coordinate.
        y (int): the y coordinate.
        id (int): the identity of the rectangle.
        Errors:
        TypeError: If either of width or height is not an int.
        ValueError: If either of width or height <= 0.
        TypeError: If either of x or y is not an int.
        ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieve it"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the coordinate x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieve it"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the coordinate y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.x, self.y, self.width, self.height))
