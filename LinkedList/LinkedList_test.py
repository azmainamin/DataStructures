import unittest
from LinkedList import Node, SingleLinkedList

class TestingSingleLinkedList(unittest.TestCase):
    # Add tests
    def test_add_addingFirstElem_savesAsHead(self):
         sl = SingleLinkedList()        
         sl.add(1)
         
         self.assertEqual(sl.head.value, 1)

    def test_add_addingSecondElem_hasLengthOfTwo(self):
         sl = SingleLinkedList()        
         sl.add(1)
         sl.add(2)
         
         self.assertEqual(len(sl), 2)
    def test_add_updatesTailCorrectly(self):
         sl = SingleLinkedList()        
         sl.add(1)
         sl.add(2)
         sl.add(100)

         self.assertEqual(sl.tail.value, 100)
    # Remove tests
    def test_remove_whenElemNotPresent_returnsFalse(self):
        sl = SingleLinkedList()

        removed = sl.remove(1)

        self.assertFalse(removed)
    def test_remove_whenElemIsHead_returnsRemovedNode(self):
        sl = SingleLinkedList()        
        sl.add(1)
        removed = sl.remove(1)

        self.assertEqual(removed.value, 1)
    def test_remove_whenElemIsTail_returnsRemovedNode(self):
        sl = SingleLinkedList()        
        sl.add(1)
        sl.add(2)
        sl.add(3)
        removed = sl.remove(3)
       
        self.assertEqual(removed.value, 3)
    def test_remove_whenElemInMiddle_returnsRemovedNode(self):
        sl = SingleLinkedList()
        sl.add(11)
        sl.add(32)
        sl.add(44)
        sl.add(99)
        removedNode = sl.remove(44)

        self.assertTrue(removedNode.value, 44)

    # Search tests
    def test_search_whenHeadIsNone_returnsFalse(self):
        sl = SingleLinkedList()
        returnValue = sl.search(1)
        self.assertEqual(False, returnValue)
    def test_search_whenItemIsAvailable_returnsNode(self):
         sl = SingleLinkedList()        
         sl.add(1)
         sl.add(2)

         item1 = sl.search(1)
         item2 = sl.search(2)
         self.assertTrue(item1.value == 1)
         self.assertTrue(item2.value == 2)

    def test_search_whenItemIsNotAvailable_returnsFalse(self):
        sl = SingleLinkedList()        
        sl.add(1)
        item2 = sl.search(2)

        self.assertEqual(item2, False)
    
    # Reverse tests
    def test_reverse_whenListReversed_returnsAppropriateHeadAndTail(self):
        sl = SingleLinkedList()
        sl.add(1)
        sl.add(2)
        sl.add(3)

        sl.reverse()
        self.assertEqual(sl.head.value, 3)
        self.assertEqual(sl.tail.value, 1)

if __name__ == '__main__':
    unittest.main()
