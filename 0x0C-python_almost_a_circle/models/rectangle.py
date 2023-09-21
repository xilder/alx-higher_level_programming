#!/usr/bin/python3
"""rectangle.py"""
from models.base import Base


class Rectangle(Base):
    """creates a subclass of Base class called rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises an instance Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # List of getter functions
    @property
    def width(self):
        """returns the width attribute"""
        return self.__width

    @property
    def height(self):
        """returns the height attribute"""
        return self.__height

    @property
    def x(self):
        """returns the x attribute"""
        return self.__x

    @property
    def y(self):
        """returns the y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """sets the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area value of the Ractangle class"""
        return self.__height * self.__width

    def display(self):
        """prints the rectangle instance in stdout using #"""

        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """string representation of the class"""

        return f"[Rectangle] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """it updates the values of the instance that calls
            this method
        """
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif kwargs and kwargs != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rect_dict = {
                        'id': self.id,
                        'width': self.width,
                        'height': self.height,
                        'x': self.x,
                        'y': self.y
                    }
        return rect_dict
