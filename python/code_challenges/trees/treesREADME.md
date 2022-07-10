# Trees
Binary trees and binary search trees in python

## Challenge
Write a binary tree and a binary search tree. The binary tree should have the functions in_order, pre_order, and post_order, which return the values of every node in the tree corresponding with each method of searching the tree. The binary search tree should have the method add to add a value in the proper place in the tree, and a method contains to efficiently find if a value is contained in the tree.

## Approach & Efficiency
Big O time for the binary tree methods of displaying all nodes: O(n) because it's directly proportional with the number of nodes in the tree. The big O for space is O(h) because the call stack never exceeds the height of the tree.
big O time for the binary search tree add method: O(H) because it always takes the most efficient path by nature of a binary search tree and so it always has to travel the height of the tree (or less). big O for space is O(1) because only one value is being appended to the tree.
big O time for the binary search tree contains method: O(H) because it always takes the most efficient path by nature of a binary search tree and so it always has to travel the height of the tree (or less). big O for space is O(1) because no values is being appended to the tree.

## API
Binary tree: pre_order(), post_order(), in_order(): no arguments, each returns the values corresponding with a method of writing the tree.
Binary search tree: add(value): adds a node with value [value] at the appropriate part of the list.
Binary search tree: contains(value): returns a boolean value expressing whether the value appears in the list or not.
