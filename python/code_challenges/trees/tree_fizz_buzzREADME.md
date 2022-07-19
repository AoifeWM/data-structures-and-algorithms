# K-ary Tree fizz buzz

Given a k-ary tree, return a NEW k-ary tree
with the standard fizz buzz protocol applied to it, plus replacing all other ints with strings of themself.


## Whiteboard Process
!(whiteboard png)[fizzbuzzwhiteboard.png]

## Approach & Efficiency
To duplicate the tree a pre-order traversal is used, and at each node we create a new node and then recursively repeat and append to the children list of the previous new node, and then iterate through the new children list for each node and do the same.
To do fizzbuzz on the new tree it is traversed breadth first and each value is tested against modulo 15, 3, 5, and if they equal 0, replace with fizzbuzz, fizz, and buzz, respectively, and if not, replace the int with a string.


## Solution
To run the code do fizz_buzz_tree(tree). The output will be a new tree with fizz buzz rules applied and ints turned to strings.
Example:
input tree:
    20
3   14   45

output tree:
       buzz
fizz   "14"  fizzbuzz


