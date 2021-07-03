from collections import Counter

import pytest

from algae.clrs.bfs import Graph, bfs_explore


def init_graph():
    g = Graph()
    g.add_edge(0, 1, 2, 3, 4, 5, 6, 7, 8)
    g.add_edge(1, 2, 3, 4, 5, 6, 7, 8)
    g.add_edge(2, 4, 6, 8)
    g.add_edge(3, 6)
    return g


@pytest.mark.parametrize(
    "graph, expected",
    [(init_graph(), Counter((0, 1, 2, 3, 4, 5, 6, 7, 8)))],
)
def test_bfs_explore(graph, expected):
    assert Counter(bfs_explore(graph)) == expected
