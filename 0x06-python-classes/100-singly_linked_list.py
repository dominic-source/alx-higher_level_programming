#!/usr/bin/python3

"""This module will create a linkedlist using pythone

Example:
    ./100-sungly_linked_list.py

"""


class Node:

    """The node class for create more nodes


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

    @data.setter
    def data(self, value):
        """set the data

        This will help set the data

        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):

        """Get the next node

        This will get the node

        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        """Set the next node

        This will set the next node

        """

        if value is None:
            pass
        elif not (isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():

    """A singly linked class

    This is the single linked list which will create and link nodes

    """

    def __init__(self):
        """initialization the singly linked list function

        """
        self.__head = None

    def sorted_insert(self, value):

        """Insert the linked list in a sorted order

        """

        if (self.__head is None) or value < self.__head.data:
            self.__head = Node(value, self.__head)

        else:
            crt = self.__head
            while(crt.next_node is not None and crt.next_node.data <= value):
                crt = crt.next_node

            if crt.next_node is None:
                newNode = Node(value)
                crt.next_node = newNode
            else:
                newNode = Node(value, crt.next_node)
                crt.next_node = newNode

    def __str__(self):

        """String representation of the class

        """

        current = self.__head
        mstr = ""
        while (current is not None):
            mstr += str(current.data)
            mstr += "\n"
            current = current.next_node

        return mstr[:-1]
