#!/usr/bin/python3

"""Module that has the base class for all other classes that will
inherit from it

"""
import json


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
