# Linked List

This code is intentionally very declarative and not refactored into smaller functions. I want the reader to follow through the code contiguously, without needing to jump between functions

## Gotchas

The biggest gotchas while coding a linked list is knowing when to stop in your while loops. Should my conditional have curr != None or curr.next != None? In the __str__(), search() and reverse() method, we want to do curr != None. Because, when curr is sitting at tail, we want the code inside the while block to execute. If we did curr.next != None, our curr will sit at tail and curr.next will point to None. So the code inside the while loop will not execute. Boo. 

But in remove(), when we are trying to find the node right before the tail, when our curr node is there, we don't want to move right anymore. When our while loop  with a conditional of rightBeforeTail.next != self.tail finishes, it means that the next node is the tail and we don't want to move anymore. 