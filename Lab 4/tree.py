"""
File: tree.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)
Contributor: Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    Implements a tree in node representation. Modified by Marinus van den Ende (m.van.den.ende.1@student.rug.nl).
"""


class TreeNode:
    def __init__(self, item=None, left=None, right=None):
        self._item = item
        self._left = left
        self._right = right

    def __copy__(self):
        """
        Returns a copy of the tree recursively
        :return: a copy of the tree
        """
        copied_item = self._item
        copied_left = self._left.__copy__() if self._left is not None else None
        copied_right = self._right.__copy__() if self._right is not None else None
        return TreeNode(copied_item, copied_left, copied_right)

    def preorder(self, action) -> None:
        """
        Performs an action for each node in the tree in preorder
        :param action: function to call for every value in the tree
        """
        action(self._item)
        if self._left is not None:
            self._left.preorder(action)
        if self._right is not None:
            self._right.preorder(action)

    def postorder(self, action) -> None:
        """
        Performs an action for each node in the tree in postorder
        :param action: function to call for every value in the tree
        """
        if self._left is not None:
            self._left.postorder(action)
        if self._right is not None:
            self._right.postorder(action)
        action(self._item)

    def inorder(self, action) -> None:
        """
        Performs an action for each node in the tree in inorder
        :param action: function to call for every value in the tree
        """
        if self._left is not None:
            self._left.inorder(action)
        action(self._item)
        if self._right is not None:
            self._right.inorder(action)

