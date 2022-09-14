# Graphs
The graph is a data structure built out of nodes (also called vertices in graphs), sort of like a linked list or a tree. But unlike those data structs, the nodes in graphs aren't restricted to only linking with specific other nodes. Any node in a graph can be linked with any other node, in either direction. In addition, 'weights' can be added to these connections: the connections themselves, (called edges), carry a value.

## Challenge
Implement a graph. The graph should be represented as an adjacency list, and should include the following methods: add node, add edge, get nodes, get neighbors, size


## Approach & Efficiency
The graph and nodes use sets to store their nodes and adjacencies, respectively. There is no top level list of adjacencies; this is stored by proxy in the set of nodes which each contain their own adjacencies.

## API
### Properties
#### Graph
* _vertices:
  * a set containing all vertices in the graph
#### Vertex
* value:
  * any value
* neighbors:
  * a set containing Edge objects
#### Edge
* vertex:
  * a Vertex. The 'end' of the edge. An Edge has no reference to its 'start' vertex.
* weight:
  * any value
### Availiable methods
#### Graph
* add_node
  * Arguments: `value`
  * Returns: The added `Vertex`
  * Adds a node to the graph with value `value`
* add_edge
  * Arguments: `start` (`Vertex`), `end` (`Vertex`), `weight` (any) = 1
  * Returns: None
  * Adds a new edge between start and end in the graph, with weight `weight`. By default, `weight` is set to 1.
  * Both nodes should already be in the Graph
* get_nodes
  * Arguments: none
  * Returns: all the nodes in the graph as a set
* get neighbors
  * Arguments: node
  * Returns: a list of edges connected to the given node
* size
  * Arguments: none
  * Returns the total number of nodes in the graph

