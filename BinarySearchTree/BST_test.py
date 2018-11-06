import unittest
from BinarySearchTree import Node, BinarySearchTree

class TestingBST(unittest.TestCase):
    # Insert tests

    def test_insert_whenInsertingFirstNode_createsRoot(self):
        bst = BinarySearchTree()
        bst.insert(1, bst.root)

        self.assertEqual(bst.root.value, 1)

    def test_insert_whenInsertingLowerValue_insertsAsLeftChild(self):
        bst = BinarySearchTree()
        bst.insert(10, bst.root)
        bst.insert(5, bst.root)

        self.assertEqual(len(bst), 2)
        self.assertEqual(bst.root.left.value, 5)
    def test_insert_whenInsertingHigherValue_insertsAsRightChild(self):
        bst = BinarySearchTree()
        bst.insert(10, bst.root)
        bst.insert(9, bst.root)
        bst.insert(15, bst.root)
        bst.insert(17, bst.root)
        
        #bst.inorderPrint(bst.root)

        self.assertEqual(len(bst), 4)
        self.assertEqual(bst.root.value, 10)
        self.assertEqual(bst.root.left.value, 9)
        self.assertEqual(bst.root.right.value, 15)
        self.assertEqual(bst.root.right.right.value, 17)

        
    # Search tests
    def test_search_whenElemNotPresent_returnsFalse(self):
        bst = BinarySearchTree()
        bst.insert(10, bst.root)
        bst.insert(9, bst.root)
        bst.insert(15, bst.root)

        #bst.inorderPrint(bst.root)

        self.assertFalse(bst.search(99, bst.root))
    def test_search_whenElemPresent_returnsTrue(self):
        bst = BinarySearchTree()
        bst.insert(10, bst.root)
        bst.insert(9, bst.root)
        bst.insert(15, bst.root)

        #bst.inorderPrint(bst.root)
        res = bst.search(15, bst.root)
        self.assertTrue(res)
    
    # Remove tests

    def test_remove_whenElemNotPresent_returnsNull(self):
        pass

    def test_remove_whenElemPresent_removesAndReturnsRemovedNode(self):
        pass

if __name__ == '__main__':
    unittest.main()