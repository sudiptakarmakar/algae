import collections
from algae.clrs.common import Graph


def bfs_explore(graph: Graph):
    visited = set()
    pipe = collections.deque()
    for src in graph.get_vertices():
        if src in visited:
            continue
        visited.add(src)
        pipe.appendleft(src)

        while pipe:
            vertex = pipe.pop()
            yield vertex
            for neighbor in graph.get_neighbors(vertex):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                pipe.appendleft(neighbor)
