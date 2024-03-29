#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """
    A rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """presents the diagram of a defined rectangle"""
        if self.__height == 0 or self.__width == 0:
            return("")
        else:
            rectangle = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += str(self.print_symbol)
                if i < self.__height - 1:
                    rectangle += "\n"
            return (rectangle)

    def __repr__(self):
        """returns a string representation of the Retangle class"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    def __del__(self):
        """prints a message when a Rectangle instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
