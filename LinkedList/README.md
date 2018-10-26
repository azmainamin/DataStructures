# Linked List

This code is intentionally very declarative and not refactored into smaller functions. I want the reader to follow through the code contiguously, without needing to jump between functions

## Gotchas

The biggest gotchas while coding a linked list is knowing when to stop in your while loops. Should my conditional have curr != None or curr.next != None? In the __str__(), search() and reverse() method, we want to do curr != None. Because, when curr is sitting at tail, we want the code inside the while block to execute. If we did curr.next != None, our curr will sit at tail and curr.next will point to None. So the code inside the while loop will not execute. Boo. 

But in remove(), when we are trying to find the node right before the tail, when our curr node is there, we don't want to move right anymore. When our while loop  with a conditional of rightBeforeTail.next != self.tail finishes, it means that the next node is the tail and we don't want to move anymore. 

## Runtime

Insertion - O(1) - Since you are either adding a head or adding to the tail. This assumes you have a pointer to both head and tail.
Deletion - O(1) - This is tricky. It's a simple O(1) if you are removing the head of a list with length 1. But if you are removing the tail or from middle, you will have to find the node right before the node you want to delete, which is O(n). But the act of removing the node itself is O(1)
Search - O(n) - Iterate the list until you find the node.
Access - O(n) - Iterate until you find the node you are looking for.