def topological_sort(graph):
    """Topological sort: DFS each node, push to stack on exit (after
    all its dependents are done), then reverse the stack.

    Use when: ordering with dependencies (course schedule, build order)
    on a DAG. A cycle means no valid ordering exists.
    Time: O(V + E). Space: O(V).
    """
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    order = topological_sort(graph)
    position = {node: i for i, node in enumerate(order)}
    for node, deps in graph.items():
        for dep in deps:
            assert position[node] < position[dep]
    print("ok")
