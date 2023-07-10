#!/usr/bin/python3

"""This module will create a linkedlist using pythone

Example:
    ./100-sungly_linked_list.py

"""


class Node:

    """The node class


    """

    def __init__(self, data, next_node=None):

        """The initialization function

        Args:
            data (int): the data
            next_node: the next node of the linked list

        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        """ Retrieve the data

        This getter will retrieve the node

        """

        return self.__data

    @data.property
    def data(self, value):
        """set the data

        This will help set the data

        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node

        This will retrieve the next node

        """
        return self.__next_node

    @next_node.property
    def next_node(self, value):
        """Set the next node

        This will set the next node of the node

        Args:
            value (Node): the node

        """

        if ((value is not None) or (not isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create the head node and add other methods to interact with the list

    """

    def __init__(self):
        """initialization of the singly linked list"""

        self.__head = Node()

    def __str__(self):
        """A single linked list"""

        current = self.__head
        while current is not None:
            print(current.data, end='')
            current = current.next_node
        return ""

    def sorted_insert(self, value):
        if self.__head.next_node == None:
            self.__head.data = value
        elif
