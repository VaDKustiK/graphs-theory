class HeapTree:
    def __init__(self):
        self.heap = []

    def insert(self, value): # adds elements to the heap and restores its properties
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def search(self, value): # finding elements in the heap
        for i, v in enumerate(self.heap):
            if v == value:
                return i  # found element index
        return -1  # element not found

    def delete(self, value): # deletes elements from the heap and restores its properties
        index = self.search(value)
        if index == -1:
            print("element not found")
            return
        
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(index)

    def heapify_down(self, index):
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            # finding index of the max child element
            max_index = child_index
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1] > self.heap[child_index]:
                max_index = child_index + 1
            
            if self.heap[index] >= self.heap[max_index]:
                break
            # changing places
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index
            child_index = 2 * index + 1

heap = HeapTree()
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(30)
print(heap.heap)

print(heap.search(15))
print(heap.search(100))

heap.delete(20)
print(heap.heap)