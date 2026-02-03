import pytest

from algs.fundamental.graphs.node import Node


def test_not_hashable():
    node = Node()

    the_set = set()

    with pytest.raises(TypeError) as exsc_info:
        the_set.add(node)

    assert "unhashable" in str(exsc_info.value)


@pytest.mark.parametrize(
    argnames=["graph1", "graph2", "are_equal"],
    argvalues=[
        # test graph 1, acyclic
        (
                Node(1, [Node(2), Node(3)]), Node(1, [Node(2), Node(3)]), True
        )
    ]
)
def test_equals(graph1: Node, graph2: Node, are_equal: bool):
    assert (graph1 == graph2) == are_equal
