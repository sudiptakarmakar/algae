from algae.clrs.common import Graph


def dfs_explore(graph: Graph):
    visited = set()

    def dfs(vertex):
        if vertex in visited:
            return
        visited.add(vertex)
        yield vertex
        for neighbor in graph.get_neighbors(vertex):
            dfs(neighbor)

    for src in graph.get_vertices():
        yield from dfs(src)
