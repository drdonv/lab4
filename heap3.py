class MaxHeap:
    heap: []
    capacity: int
    size: int

    def __init__(self, capacity=None):
        self.heap = []
        self.capacity = capacity
        self.size = 0

    # enqueue int -> bool
    # This method takes in an integer and enqueues it into the heap
    def enqueue(self, item):
        if self.size == 0:
            self.heap[0] = item
            self.size += 1

        else:
            index = 0
            while index in range(self.get_capacity()):
                if index > self.get_capacity():
                    return False
                if self.heap[index] is None:
                    self.heap[index] = item
                    self.size += 1
                    break
                index += 1
            self.perc_up(index)
        return True

    # peek None -> int
    # This method returns the max value of the heap (the first one)
    def peek(self):
        if self.heap[0] is None:
            return None
        return self.heap[0]

    # dequeue None -> int
    # This method removes the max value (the first one) and re-ensures the heap is valid
    def dequeue(self):
        max = self.heap[0]
        size = self.get_size()
        self.heap[0] = self.heap.pop(size-1)
        self.perc_down(0)
        return max

    # contents None -> List[int]
    # This returns the heap in the form of a list, without any trailing None values
    def contents(self):
        heaplist = []
        for i in self.heap:
            if i is not None:
                heaplist.append(i)
        return heaplist

    # build_heap List[int] -> None
    # This takes a list as an input and builds a max heap of it.
    def build_heap(self, alist):
        capacity = self.get_capacity()
        if capacity is not None:
            self.heap = [None] * capacity
        else:
            self.heap = [None] * len(alist)
            self.capacity = len(alist)
        for i in alist:
            self.enqueue(i)

    # is_empty None -> bool
    # This method checks if the heap is empty by checking if the size is 0. True if it is, False if not.
    def is_empty(self):
        return self.size == 0

    # is_full None -> bool
    # This method checks if the heap is full by checking if the size is equal to the capacity
    def is_full(self):
        return self.size == self.capacity

    # get_capacity None -> int
    # Returns the capacity property of the MaxHeap
    def get_capacity(self):
        return self.capacity

    # get_size None -> int
    # Returns the size property of the MaxHeap
    def get_size(self):
        count = 0
        for i in self.heap:
            if i is not None:
                count += 1
        return count

    # perc_down int -> None
    # This method takes the input of an index of the heap, then percs the value in that index down as necessary to keep the MaxHeap properties true.
    def perc_down(self, i):
        heap = self.heap
        left_child = (2 * i) + 1
        right_child = (2 * i) + 2
        while (2 * i) + 2 < self.get_capacity() and (heap[i] < heap[left_child] or heap[i] < heap[right_child]):
            if heap[i] < heap[left_child]:
                l_child = heap[left_child]
                heap[left_child] = heap[i]
                heap[i] = l_child
                i = 2 * i + 1
            elif heap[i] < heap[right_child]:
                r_child = heap[right_child]
                heap[right_child] = heap[i]
                heap[i] = r_child
                i = 2 * i + 2
            left_child = (2 * i) + 1
            right_child = (2 * i) + 2

    # perc_up int -> None
    # This method takes the input of an index of the heap, then percs the value in that index up as necessary to keep the MaxHeap properties true.
    def perc_up(self, i):
        while i < self.get_size() and (i - 1) // 2 >= 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    # heap_sort_ascending List[int] -> None
    # Sorts a list in ascending order, then builds a heap with it.
    def heap_sort_ascending(self, alist):
        alist.sort()

        self.build_heap(alist)
