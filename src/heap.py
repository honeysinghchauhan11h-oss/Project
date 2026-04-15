class MinHeap:
    """
    Array-based Min-Heap.
    Parent is always <= children.
    Supports O(log n) insert and extract_min.
    """

    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def insert(self, priority, item):
        self.heap.append((priority, item))
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent][0]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _bubble_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
