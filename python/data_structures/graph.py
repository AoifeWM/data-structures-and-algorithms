class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self._vertices = set()

    def add_node(self, value):
        new = Vertex(value)
        self._vertices.add(new)
        return new

    def add_edge(self, start, end, weight=1):
        '''

        '''
        if start not in self._vertices:
            raise KeyError("start node not found", start)
        if end not in self._vertices:
            raise KeyError("end node not found", end)
        if weight == 0:
            raise ValueError("weight cannot be 0")
        new = Edge(end, weight)
        start.neighbors.add(new)

    def remove_edge(self, start, end):
        """
        arguments: start (Node), end (Node)
        \n removes an edge between the two supplied nodes (vertices)
        """
        if start not in self._vertices:
            raise KeyError("start node not found", start)
        if end not in self._vertices:
            raise KeyError("end node not found", end)
        for edge in start.neighbors:
            if edge.end == end:
                start.neighbors.remove(edge)
        raise KeyError("edge not found", start, end)

    def get_nodes(self):
        if self._vertices:
            return self._vertices

    def get_neighbors(self, node):
        if node.neighbors:
            return list(node.neighbors)

    def size(self):
        return len(self._vertices)


class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbors = set()


class Edge:

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight



# gp = Graph()
# node = gp.add_node(Vertex(5))
# node2 = gp.add_node(Vertex(4))
# print(gp.remove_edge(node, node2))
# print(gp.add_edge(node, node2, 5))

# gp = Graph()
# print(gp.get_vertices())
# node = gp.add_vertex(Vertex(5))
# node2 = gp.add_vertex(Vertex(4))
# print(gp.add_edge(node, node2, 5))
# print(gp.size())
# print(gp.remove_edge(node, node2))
# print(gp.size())
