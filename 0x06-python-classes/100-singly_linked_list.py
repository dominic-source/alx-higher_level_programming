#!/usr/bin/python3

"""This module will create a linkedlist using pythone

Example:
    ./100-sungly_linked_list.py

"""


class Node:

    """The node class


    """

    def __init__(self, data, next_node):

        """The initialization function

        Args:
            data (int): the data
            next_node: the next node of the linked list

        """

        self.data = data
        self.new_node = next_node

    @property
    def data(self):

        """ Retrieve the data

        This getter will retrieve the node

        """

        return self.__data

    @data.property
    def data(self):
        """set the data

        This will help set the data

        """
        self.__data = data
