class MinHeap:
    def __init__(self):
        self.heap = []

    def enqueue(self, item):
        self.heap.append(item)
        self._upheap(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")
        elif len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._downheap(0)
        return min_val

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _upheap(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._upheap(parent_index)

    def _downheap(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] < self.heap[smallest]):
            smallest = left_child_index

        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] < self.heap[smallest]):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._downheap(smallest)

    def print_heap(self):
        self._print_heap(0, 0)

    def _print_heap(self, index, depth):
        if index < len(self.heap):
            self._print_heap(2 * index + 2, depth + 1)
            print('\t' * depth + str(self.heap[index]))
            self._print_heap(2 * index + 1, depth + 1)


# Example Usage:
if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.enqueue(4)
    min_heap.enqueue(2)
    min_heap.enqueue(7)
    min_heap.enqueue(5)
    min_heap.enqueue(1)
    min_heap.enqueue(9)
    min_heap.enqueue(3)

    print("Heap elements:")
    min_heap.print_heap()

    print("Popping elements:")
    while len(min_heap.heap) > 0:
        print(min_heap.dequeue())
