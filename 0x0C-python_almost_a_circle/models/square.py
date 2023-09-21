#!/usr/bin/python3
"""square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creates an instance of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialises the square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """defines a format for its string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """returns the size of the element"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """it updates the values of the instance that calls
            this method
        """
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif kwargs and kwargs != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the square class"""
        sq_dict = {
                    'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y
                    }
        return sq_dict
