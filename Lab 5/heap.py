class Heap:
    def __init__(self):
        self._heap = [0]

    def size(self) -> int:
        return len(self._heap) - 1

    def _heap_empty_error(self) -> None:
        print("Heap empty")

    # Exercise 3.10
    def _upheap(self, index: int) -> None:
        if index > 1:
            parent_index = index // 2
            if self._heap[parent_index] < self._heap[index]:
                self._heap[parent_index], self._heap[index] = self._heap[index], self._heap[parent_index]
                self._upheap(parent_index)

    def enqueue(self, value) -> None:
        self._heap.append(value)
        self._upheap(self.size())

    # Exercise 3.11
    def _downheap(self, index: int) -> None:
        lc = index * 2
        rc = lc + 1
        if lc < self.size():
            value = self._heap[index]

            left_child = self._heap[lc]

            if self._heap[lc] and self._heap[rc]:
                right_child = self._heap[rc]
            else:
                right_child = left_child

            if left_child > value and left_child >= right_child:
                self._heap[lc], self._heap[index] = self._heap[index], self._heap[lc]
                self._downheap(lc)
            elif right_child > value:
                self._heap[rc], self._heap[index] = self._heap[index], self._heap[rc]
                self._downheap(rc)

    def remove_max(self):
        return_value = self._heap[1]
        if self.size() > 1:
            self._heap[1] = self._heap.pop()
            self._downheap(1)
        else:
            self._heap.pop()
        return return_value
