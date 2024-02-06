"""
File:   queue.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    A queue implemented as a Python list
"""


class Queue:
    """
    Creates a first-in-first-out (FIFO) queue
    """

    def __init__(self):
        self._q = [0, 0]
        self._front = 0
        self._back = 0

    def size(self) -> int:
        """
        Returns the number of items in the queue
        :return: number of items in the queue
        """
        size = self._back - self._front
        if self._front > self._back:
            size += len(self._q)
        return size

    def dequeue(self):
        """
        Removed and returns the oldest item in the queue
        :return: the item that has been in the queue the longest
        """
        if self.size() == 0:
            print("Queue empty!")
            return None
        item = self._q[self._front]
        self._front = (self._front + 1) % len(self._q)
        return item

    def enqueue(self, item) -> None:
        """
        Adds an item to the end of the queue
        :param item: item to add to the queue
        """
        self._q[self._back] = item
        self._back = (self._back + 1) % len(self._q)
        if self._back == self._front:
            self._back += len(self._q)
            self._q.extend(self._q)
