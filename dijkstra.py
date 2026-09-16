import heapq


def dijkstra(graph, start):
    """Dijkstra: shortest paths from start via a min-heap of (dist, node).

    Use when: weighted graph with non-negative edges, "cheapest/shortest
    cost to reach X". graph[node] is a list of (neighbor, weight).
    Time: O(E log V). Space: O(V).
    """
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist


if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    assert dijkstra(graph, "A") == {"A": 0, "B": 1, "C": 3, "D": 4}
    print("ok")
