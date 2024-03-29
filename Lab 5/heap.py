"""
File: heap.py
Authors: Marcus Persson (m.h.o.persson@student.rug.nl), Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A heap data structure implementation.
"""

"""

Left child = 2k
right child = 2k + 1
"""


class Heap:
    def __init__(self):
        self._heap = [0]
        self.positions = []

    def size(self) -> int:
        return len(self._heap) - 1

    def _heap_empty_error(self) -> None:
        print("Heap empty")

    def enqueue(self, value) -> None:
        self.positions.append(self.size() + 1)
        self._heap.append(value)
        self._upheap(self.size())

    def _parent_node(self, index: int) -> int:
        return self._heap[index // 2]

    def left_child_node(self, index: int) -> int:
        return self._heap[index * 2]

    def right_child_node(self, index: int) -> int:
        return self._heap[(index * 2) + 1]

    def _swap(self, left: int, right: int) -> None:
        # need to minus one from both left and right because heap does not use the first element.
        # Needs to be swapped with element of the parent index

        left_index = self.positions.index(left)
        right_index = self.positions.index(right)

        self.positions[left_index], self.positions[right_index] = self.positions[right_index], self.positions[left_index]

    def _upheap(self, index: int) -> None:
        if index > 1:
            parent = self._parent_node(index)
            if parent > self._heap[index]:
                self._heap[_parent_index(index)] = self._heap[index]
                self._heap[index] = parent
                self._swap(index, _parent_index(index))
                self._upheap(_parent_index(index))

    def remove_min(self):
        return_value, position = self._heap[1], self.positions.index(1)
        if self.size() > 1:
            self._swap(1, self.size())
            index = self.positions.index(self.size())
            self.positions[index] = 0
            self._heap[1] = self._heap.pop()
            self._downheap(1)
        else:
            self._heap.pop()
        return return_value, position

    def get_min(self) -> (int, int):
        return self._heap[1], self.positions.index(1)

    def get_weight_from_key(self, pos: int) -> float:
        return self._heap[self.positions[pos]]

    def set_weight_from_key(self, pos: int, weight: float) -> None:
        self._heap[self.positions[pos]] = int(weight)
        self._upheap(self.positions[pos])

    def _downheap(self, node: int) -> None:

        left = left_child_index(node)
        right = right_child_index(node)

        if left < len(self._heap):
            lc = self.left_child_node(node)
            if right < len(self._heap):
                rc = self.right_child_node(node)
            else:
                rc = self.left_child_node(node)

            if lc < self._heap[node] and lc <= rc:
                self._swap(left, node)
                self._heap[left], self._heap[node] = self._heap[node], lc
                self._downheap(left)
            elif rc < self._heap[node]:
                self._swap(right, node)
                self._heap[right], self._heap[node] = self._heap[node], rc
                self._downheap(right)

    def print_heap(self) -> None:
        # Handle empty heap
        if self.size() == 0:
            print("Heap is empty")
            return

        # The level represents the current level in the heap we are on, starting from 1
        level = 1
        while True:
            # Calculate the number of elements at the current level
            level_count = 2 ** (level - 1)
            # Calculate the start and end index of the current level in the heap
            start_index = 2 ** (level - 1)
            end_index = min(start_index + level_count, len(self._heap))

            # Extract the current level's elements from the heap
            current_level = self._heap[start_index:end_index]

            # Break the loop if the current level is empty
            if not current_level:
                break

            # Print the current level's elements
            print("Level", level, ":", ' '.join(map(str, current_level)))

            # Go to the next level
            level += 1

        # Positions list for debugging
        print("Positions:  ", end= "")
        for i in range(len(self.positions)):
            print(i, end=", ")
        print()
        print("Positions:", self.positions)

    def deep_copy(self):
        new_heap = Heap()
        new_heap._heap = [item for item in self._heap]
        new_heap.positions = [pos for pos in self.positions]

        return new_heap


def _parent_index(index: int) -> int:
    return index // 2


def left_child_index(index: int) -> int:
    return index * 2


def right_child_index(index: int) -> int:
    return (index * 2) + 1
