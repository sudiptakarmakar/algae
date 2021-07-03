import collections


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"TreeNode<{self.val}>"

    def __eq__(self, other):
        return self.val == other.val if other is not None else self is None

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self != other:
            return other is None or self.val > other.val
        return False

    def __repr__(self):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"ListNode<{self.val}>"


class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(set)

    def add_edge(self, src: int, *dst: int):
        if dst:
            self.edges[src].update(dst)
        for v in dst:
            self.edges[v].add(src)

    def get_neighbors(self, vertex: int):
        return self.edges[vertex]

    def get_vertices(self):
        return self.edges.keys()

    def __repr__(self):
        return "\n".join([f"{k} --> {v}" for k, v in self.edges.items()])


class DiGraph:
    def __init__(self):
        self.out_edges = collections.defaultdict(set)
        self.in_edges = collections.defaultdict(set)

    def add_edge(self, src: int, *dst: int):
        if dst:
            self.out_edges[src].update(dst)
        for v in dst:
            self.in_edges[v].add(src)

    def get_out_neighbors(self, vertex: int):
        return self.out_edges[vertex]

    def get_in_neighbors(self, vertex: int):
        return self.in_edges[vertex]

    def get_vertices(self):
        return self.out_edges.keys() | self.in_edges.keys()

    def __repr__(self):
        return "\n".join([f"{k} --> {v}" for k, v in self.out_edges.items()])
