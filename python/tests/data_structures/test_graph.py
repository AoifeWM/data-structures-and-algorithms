import pytest
from data_structures.graph import Graph, Vertex


def test_exists():
    assert Graph


# @pytest.mark.skip("TODO")
def test_add_node():

    graph = Graph()

    expected = "spam"  # a vertex's value that comes back

    actual = graph.add_node("spam").value

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_edge():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "banana"
    assert neighbors[0].weight == 5


# @pytest.mark.skip("TODO")
def test_bouquet():
    g = Graph()
    apple = g.add_node("apple")
    g.add_edge(apple, apple, 10)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "apple"
    assert neighbors[0].weight == 10


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    loner = Vertex("loner")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == "banana"

    assert neighbor_edge.weight == 44


def test_get_nodes_empty():

    graph = Graph()

    expected = None

    actual = graph.get_nodes()

    assert actual == expected


def test_depth_first():
    gp = Graph()
    node = gp.add_node("a")
    node2 = gp.add_node("b")
    node3 = gp.add_node("c")
    node4 = gp.add_node("d")
    node5 = gp.add_node("e")
    node6 = gp.add_node("f")
    node7 = gp.add_node("g")
    node8 = gp.add_node("h")
    gp.add_edge(node, node2)
    gp.add_edge(node2, node)
    gp.add_edge(node, node4)
    gp.add_edge(node4, node)
    gp.add_edge(node2, node3)
    gp.add_edge(node3, node7)
    gp.add_edge(node3, node2)
    gp.add_edge(node7, node3)
    gp.add_edge(node4, node5)
    gp.add_edge(node5, node4)
    gp.add_edge(node4, node6)
    gp.add_edge(node6, node4)
    gp.add_edge(node4, node8)
    gp.add_edge(node8, node4)

    actual = [node, node4, node8, node6, node5, node2, node3, node7, ]
    expected = gp.depth_first(node)
    parsed = [item.value for item in expected]
    print("\n\n", parsed, "\n\n")
    assert len(actual) == len(expected)
    for item in actual:
        assert item in expected
