import unittest
from minHeap import MinHeap

class TestingSingleLinkedList(unittest.TestCase):
    def test_add_AddsElemToHeap(self):
        minHeap = MinHeap()
        minHeap.add(3)
        firstItem = minHeap.heap[0]
        self.assertEqual(firstItem, 3)

    def test_convertArrayToHeap_MaintainsHeapOrder(self):
        minHeap = MinHeap()
        arr = [3,9,12,7,1]
        expectedHeap = [1,3,12,9,7]
        res = minHeap.convertArrayToHeap(arr)
        self.assertListEqual(expectedHeap, res)

    def test_remove_removesElemAndMaintainsHeapProperty(self):
        minHeap = MinHeap()
        arr = [3,9,12,13,1]
        _ = minHeap.convertArrayToHeap(arr)
        minHeap.remove(13)
        expectedHeap = [1, 3, 12, 9]
        
        self.assertListEqual(expectedHeap, minHeap.heap)


if __name__ == '__main__':
    unittest.main()