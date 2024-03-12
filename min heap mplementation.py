class minheap:
    def __init__(self):
        self.heap = []
    def insert(self,data):
        self.heap.append(data)
        self.heap.heapify_up(len(self.heap) -1)

    def heapify_up(self,index):
        parent_index = (index -1) //2

        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
            self.heapify_up(parent_index)

    def heapify_down(self,index):
        lchild_idx  =  2 * index + 1
        rchild_idx = 2 * index + 2
        smallest = index
        if lchild_idx < len(self.heap) and self.heap[lchild_idx] < self.heap[index]:
            smallest = lchild_idx
        if rchild_idx < len(self.heap) and self.heap[rchild_idx] < self.heap[index]:
            smallest  = rchild_idx
        if smallest != index:
            self.heap[smallest],self.heap[index] = self.heap[index],self.heap[smallest]
            self.heapify_down(smallest)


    def delete(self,val):
        if val in self.heap:
            index = self.heap.index(val)
            last = self.heap.pop()
            if index < len(self.heap):
                self.heap[index] = last
                self.heapify_down(index)
                self.heapify_up(index)
    def deleteroot(self):
        if self.heap is None:
            print("Not possible")
        else:
            last  = self.heap.pop()
            if self.heap:
                self.heap[0] = last
                self.heapify_down(0)
            return last

    def extract_min(self):
        if self.heap is None:
            print("The heap is empty")
        else:
            last = self.heap.pop()
            if self.heap:
                self.heap[0] = last
                self.heapify_down(0)
            return last
