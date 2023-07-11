#!/usr/bin/python3


"""A module that has a function to read a file

"""


def read_file(filename=""):
    """This will open the file and read out the bytes for printing

    """

    with open(filename, encoding="UTF-8") as file:
              myfile = file.read()
              print(myfile, end="")
