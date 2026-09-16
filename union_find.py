class UnionFind:
    """Disjoint Set Union with path compression + union by rank.

    Use when: connectivity/grouping queries (are these connected?
    number of connected components), Kruskal's MST, detecting cycles
    in an undirected graph.
    Time: ~O(1) amortized per op (inverse Ackermann). Space: O(n).
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.find(0) == uf.find(2)
    assert uf.find(0) != uf.find(3)
    uf.union(3, 4)
    assert uf.find(3) == uf.find(4)
    print("ok")
