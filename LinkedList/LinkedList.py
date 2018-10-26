
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SingleLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        self.count = 0

    def __len__(self):
        return self.count
        
    def __str__(self):
        toPrint = ""
        curr = self.head
        
        while curr is not None: #Why not curr.next != None? Because, then we our curr will be at tail but we don't print its value
            toPrint += f"{curr.value}, "
            curr = curr.next
        return toPrint

    def add(self, value):
        nodeToAdd = Node(value)

        # If empty LinkedList
        if self.head is None:
            self.head = nodeToAdd
        else:
            self.tail.next = nodeToAdd

        self.tail = nodeToAdd
        self.count += 1

    def remove(self, value):
        
        hasItem = self.search(value)
        
        # If removing head    
        if hasItem:
            if value == self.head.value:
                removed = self.head
                self.head = self.head.next
                return removed
            # If removing tail
            if value == self.tail.value:
                # Need to find the node right before tail
                rightBeforeTail = self.head
                while rightBeforeTail.next != self.tail: #Why rightBeforeTail.next here? Because we just want to find that node and don't do anything
                    rightBeforeTail = rightBeforeTail.next
                
                removed = self.tail
                self.tail = rightBeforeTail
                             
                return removed
            # Removing from middle
                # Find the node right before
            rightBefore = self.head
            while rightBefore.next.value != value and rightBefore.next is not None:
                rightBefore = rightBefore.next
            
            removed = rightBefore.next
            rightBefore.next = rightBefore.next.next
            return removed 
            

        return False
    def search(self, value):        
        curr = self.head
        while curr is not None and curr.value != value: 
            curr = curr.next

        if curr == None:
            return False

        return curr
        
    def reverse(self):
        """
        Algo: Initialize prev as None, as the new tail (old head)'s 'next' pointer will point to this.
        Then save curr.next to a temp variable and move curr and prev one step to the right, while 
        changing curr.next to point backwards i.e. to prev. Keep doing it until we reach the end.
        """
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.tail = self.head
        self.head = prev

def main():
    sl = SingleLinkedList()
    sl.add(1)
    sl.add(2)
    sl.add(3)
    sl.add(4)
    sl.reverse()
    print(sl)

if __name__ == "__main__":
    main()