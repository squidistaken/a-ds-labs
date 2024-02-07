"""
File:   stack.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    A stack implemented as a Python list
"""


class Stack:
    """
    Creates a stack that allows for last-in-first-out (LIFO) access
    """

    def __init__(self):
        self._stack = []

    def push(self, item) -> None:
        """
        Adds an item to the top of the stack
        :param item: item to add
        """
        self._stack.append(item)

    def pop(self):
        """
        Removes and returns the item on top of the stack
        :return: item on top of the stack
        """
        return self._stack.pop()

    def size(self) -> int:
        """
        Returns the number of items on the stack
        :return: number of items on the stack
        """
        return len(self._stack)


