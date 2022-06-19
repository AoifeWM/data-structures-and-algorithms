# Stacks and Queues
This is a simple python implementation of a stack and a queue method

## Challenge
Write classes for Stack and Queue that can add new values, remove values, check if it's empty, and check the first value of the list.

## Approach & Efficiency
Big O of time for the value adding methods is O(1) because they don't require traversal through the list so it doesn't matter what size it is.

## API
STACK:
* push: Add a new value to the top of the stack. Argument is value for the new node.
* Pop: remove a value from the top of the stack and return its value upon completion. Stack must have items to use
* is_empty: check if the stack is empty or not. returns boolean
* Peek: show first value of the stack. Stack must have items to use

QUEUE:
* Enqueue: add a new item to the front of the queue. Argument is the value for the new node
* Dequeue: remove an item from the front of the queue. Return its value after completion. Queue must have items to use this method.
* is_empty: check if the queue is empty or not. Returns boolean
* peek: show value of the front node of the queue. Queue must have items to use this method.
