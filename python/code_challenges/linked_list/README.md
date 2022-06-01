# Singly Linked List
This is a simple implementation of a singly linked list in python. It functions a lot like a list but the memory it takes up is non-contiguous, so it's better for certain applications, like large data storage (because it won't have to read/write the entire list if the length is substantially increased and it no longer fits in its current space in memory; the new nodes will just be placed wherever is free in memory, so the original list can stay in place).

## Challenge
Write a system of linked lists which can be manually constructed with node objects, can insert new nodes, can check to see if the entire list includes a given value or not, and can output the entire list as a formatted string.

## Approach & Efficiency
Big O time for this approach is O(1) because only 2 objects are being manipulated, no matter the size of the list: The head value of the linked list, the new node object that's being inserted. Everything else remains the same.
Big O space for this approach is O(n) because the space the list takes up is linearly proportional with the number of values in the list.

## API
Availiable Classes and methods:
* LinkedList
  * Props:
    * `head` (stores reference to first item in the list)
  * Methods:
    * `insert(value)`:
      * inserts a new node with `value` as its value at the head of the list.
    * `includes(value)`
      * returns a boolean based on if `value` appears anywhere in the list (`True` if it *is* included)
    * `to_string()`
      * returns the entire linked list as a string formatted like this: `"{ node1.value } -> { node2.value } -> { node3.value } -> NULL"`
* Node
  * Props:
    * `value` (stores a value)
    * `next` (stores a reference to the next node in the list. `None` by default. Nodes at the end of lists should have `None` for this property)
