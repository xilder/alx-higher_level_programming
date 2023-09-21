#!/usr/bin/python3

"""base.py
"""
import json
import csv
import turtle


class Base:
    """the base model for this programme
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        if (not isinstance(list_dictionaries, list) or not
                all(isinstance(i, dict) for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="UTF-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                list_dicts = [inst.to_dictionary() for inst in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json string representation in the argument"""

        if json_string is not None and json_string != "":
            if not isinstance(json_string, str):
                raise TypeError("input must be a string")
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of the class with all the attributes set"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        if cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of classes from a file of json string"""

        filename = cls.__name__ + "json"
        try:
            with open(filename, "r", encoding="UTF-8") as f:
                instances = Base.from_json_string(f.read())
                return [cls.create(**dict_) for dict_ in instances]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of a class' instances to a csv file"""

        filename = cls.__name__ + "json"
        with open(filename, "w", encoding="UTF-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    column_name = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    column_name = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=column_name)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads a class' instances from a csv file"""
        filename = cls.__name__
        try:
            with open(filename, "r", encoding="UTF-8") as f:
                if cls.__name__ == "Rectangle":
                    column_name = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    column_name = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=column_name)
                instances = [dict([k, int(v)] for k, v in d.items())
                             for d in list_dicts]
                return [cls.create(**d) for d in instances]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangle and square instances in the turtle mode"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
