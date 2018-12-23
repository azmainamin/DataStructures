class MinHeap:
    def __init__(self, array = []):
        self.array = array
        self.heap = []
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.heap)

    def add(self,val):
        # Add item to end
        self.heap.append(val)
        self.count += 1

        # Heapify/Bubble up
        self.bubbleUp()

    def convertArrayToHeap(self, arr):
        for item in arr:
            self.add(item)

        return self.heap

    def bubbleUp(self):
        """
        While curr elem is smaller than it's parent elem, keep swapping till you hit the root
        """
        lastIndex = self.count - 1
        parentIndex = self._getParentIndex(lastIndex)

        while lastIndex > 0 and self.heap[lastIndex] < self.heap[parentIndex]:
            self._swap(lastIndex, parentIndex)
            lastIndex = parentIndex
            parentIndex = self._getParentIndex(lastIndex)

    def search(self, val):
        for i in range(len(self.heap)):
            if self.heap[i] == val:
                return i

        return -1 
    
    def remove(self, val):
        # Find index of val to be removed
        idx = self.search(val)

        if idx == -1:
            return -1 

        # Swap the last elem with elem at idx
        self._swap(idx, -1)
        self.heap.pop(-1)
        self.count -= 1

        # Bubble down the elem we swapped if needed
        self.bubbleDown(idx)

    def bubbleDown(self, idx):
        """
        While curr elem is bigger than its left or right child, swap with the smaller of the two.
        Make sure the left and right index in the while loop is in bounds
        """
        while (self._getLeftChildIndex(idx) < self.count and self._getRightChildIndex(idx) < self.count) and (self.heap[idx] > self._getLeftChild(idx) or self.heap[idx] > self._getRightChild(idx)):
            # Take the smallest value from left or right
            if self._getLeftChild(idx) < self._getRightChild(idx):
                leftIdx = self._getLeftChildIndex(idx)
                self._swap(idx, leftIdx)
                idx = leftIdx
            else:
                rightIdx = self._getRightChildIndex(idx)
                self._swap(idx, rightIdx)
                idx = rightIdx        

    def _swap(self, i, j):
        """
        i, j - Indices of values to be swapped
        """
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def _getLeftChild(self, i):
        return self.heap[self._getLeftChildIndex(i)]

    def _getRightChild(self, i):
        return self.heap[self._getRightChildIndex(i)]

    def _getLeftChildIndex(self, i):
        return 2*i + 1

    def _getRightChildIndex(self, i):
        return 2*i + 2
    
    def _getParent(self, i):
        return self.heap[self._getParentIndex(i)]

    def _getParentIndex(self, i):
        return (i-1)//2


