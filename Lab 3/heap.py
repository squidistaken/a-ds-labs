class Heap:
    def __init__(self):
        self._heap = [0]

    def size(self) -> int:
        return len(self._heap) - 1

    def _heap_empty_error(self) -> None:
        print("Heap empty")

    def _upheap(self, index: int) -> None:
        pass

    def enqueue(self, value) -> None:
        self._heap.append(value)
        self._upheap(len(self._heap))

    def _downheap(self, index: int) -> None:
        pass

    def remove_max(self):
        return_value = self._heap[1]
        self._heap[1] = self._heap.pop()
        self._downheap(1)
        return return_value


