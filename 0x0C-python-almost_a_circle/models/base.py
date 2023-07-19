#!/usr/bin/python3

"""Module that has the base class for all other classes that will
inherit from it

"""
import json
import csv
import turtle
import random


class Base:
    """The base class named as Base for readability purposes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method"""
        if id is not None:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert json to string"""

        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string into file"""

        new_list = []
        if list_objs is None:
            string = '[]'
        else:
            for i in list_objs:
                new_list.append(i.to_dictionary())
            string = cls.to_json_string(new_list)
        clasname = cls.__name__ + '.json'

        with open(clasname, 'w', encoding='utf-8') as file2:
            file2.write(string)

    @staticmethod
    def from_json_string(json_string):
        """convert from json string"""

        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a dictionary"""

        if dictionary is None:
            return None
        if cls.__name__ == "Square":
            dummycls = cls(4)
        else:
            dummycls = cls(4, 5)
        dummycls.update(**dictionary)
        return dummycls

    @classmethod
    def load_from_file(cls):
        """load from file"""
        new_list = []
        clasname = cls.__name__ + '.json'
        try:
            with open(clasname, 'r', encoding='utf-8') as file2:
                my_file = file2.read()
                jsonvalue = cls.from_json_string(my_file)
        except FileNotFoundError:
            return new_list
        for i in jsonvalue:
            new_list.append(cls.create(**i))
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save file to csv"""

        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(i.to_dictionary())
            fieldnames = list(new_list[0].keys())

        clasname = cls.__name__ + '.csv'

        with open(clasname, 'w', newline='') as file2:
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_list)

    @classmethod
    def load_from_file_csv(cls):
        """load csv file """

        new_list = []
        clasname = cls.__name__ + '.csv'

        try:
            with open(clasname, 'r') as file3:
                reader = csv.DictReader(file3)
                for row in reader:
                    for i in row:
                        row[i] = int(row[i])
                    new_list.append(cls.create(**row))
        except FileNotFoundError:
            return new_list

        return new_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw graphics in python"""

        colors = ["red", "blue", "green", "indigo",
                  "black", "pink", "purple", "orange", "brown"]
        count = 0
        screen = turtle.Screen()
        for rect in list_rectangles:
            turt = turtle.Turtle()
            values = rect.to_dictionary()
            count += 1

            # Select colors
            turt.color(random.choice(colors), random.choice(colors))

            # Pen up and position the shape
            turt.pu()
            turt.goto(values["x"], values["y"])
            turt.pd()

            # Draw the shape
            turt.begin_fill()
            turt.forward(values["width"])
            turt.right(90)
            turt.forward(values["height"])
            turt.right(90)
            turt.forward(values["width"])
            turt.right(90)
            turt.forward(values["height"])
            turt.pu()
            turt.end_fill()

            # additions to make it more interesting
            for i in range(5):
                turt.goto(random.randint(-300, -100), random.randint(1, 200))
                turt.pd()
                turt.begin_fill()
                turt.circle(20)
                turt.color(random.choice(colors))
                turt.end_fill()
                turt.pu()

        for squa in list_squares:
            turt2 = turtle.Turtle()
            values = squa.to_dictionary()
            count += 1

            # Select colors
            turt.color(random.choice(colors), random.choice(colors))

            # Pen up and position the shape
            turt.pu()
            turt.goto(values["x"], values["y"])
            turt.pd()

            # Draw the shape
            turt.begin_fill()
            turt.forward(values["size"])
            turt.right(90)
            turt.forward(values["size"])
            turt.right(90)
            turt.forward(values["size"])
            turt.right(90)
            turt.forward(values["size"])
            turt.pu()
            turt.end_fill()

            # additions to make it more interesting
            for i in range(5):
                turt.goto(random.randint(100, 300), random.randint(-300, -200))
                turt.pd()
                turt.begin_fill()
                turt.circle(20)
                turt.color(random.choice(colors))
                turt.end_fill()
                turt.pu()
        turtle.done()
