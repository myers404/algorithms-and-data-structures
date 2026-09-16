from collections import deque


def bfs(graph, start):
    """Breadth-first search: explore level by level via a queue.

    Use when: shortest path in an unweighted graph, level-order
    processing, "fewest steps/edges to reach X".
    Time: O(V + E). Space: O(V).
    """
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, start, visited=None, order=None):
    """Depth-first search: explore as far as possible via recursion/stack.

    Use when: connectivity, cycle detection, path existence,
    exhaustive exploration, or as the base for topological sort.
    Time: O(V + E). Space: O(V) (call stack).
    """
    if visited is None:
        visited = set()
        order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    assert bfs(graph, "A") == ["A", "B", "C", "D"]
    assert dfs(graph, "A") == ["A", "B", "D", "C"]
    print("ok")
