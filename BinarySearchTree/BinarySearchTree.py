class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def inorderPrint(self, root):
        if root is not None:
            self.inorderPrint(root.left)
            print(f"\nNode: {root.value}")
            self.inorderPrint(root.right)

    def insert(self, value, root):       
        if self.root is None: # empty bst
            nodeToAdd = Node(value)
            self.root = nodeToAdd
            self.count += 1
        else:          
            if value < root.value:
                if root.left is None: # no more nodes on left, so add it here
                    nodeToAdd = Node(value)
                    root.left = nodeToAdd
                    self.count +=1
                else: # has left subtree, so you need to go deeper until you find the spot to add the node
                    self.insert(value, root.left)
            else:
                if root.right is None:
                    nodeToAdd = Node(value)
                    root.right = nodeToAdd
                    self.count += 1
                else:
                    self.insert(value, root.right)

    def search(self, value, root):       
        if root is None:
            return False
                
        if value == root.value:
            return True
        else:
            if value < root.value:
                return self.search(value, root.left) # spent an hour debugging because I did not have the return statemeny here.
            else:
                return self.search(value, root.right)

    def remove(self, value):
        pass
    def findParent(self, value):
        pass
    
