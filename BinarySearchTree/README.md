# Binary Search Tree

This code is intentionally very declarative and not refactored into smaller functions. I want the reader to follow through the code contiguously, without needing to jump between functions. Also, the if-else blocks are verbose intentionally as well, to keep the flow readable.

## Gotchas
The biggest gotcha was the recursive calls. I always have a hard time visualizing the recursive call stack.

1. Search - I spent a good hour or so trying to figure out why my function was returning None when I only have it returning either True or False. There were no 'return None' statements! 

What I forgot to realize was that when we do recursive calls, the return value at the base case(s) need to be propagated up/down to the initial function call. Since I was not returning the return value of the recursive call, the initial call had no return statement (as it does not satisfy the base case conditionals), thus returning None implicitly.

This problem is not present in insert() as it does not return anything. 


## Runtime

Insert - O(log n)
Search - O(log n)