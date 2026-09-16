import heapq


def top_k_largest(arr, k):
    """Heap top-K: keep a min-heap of size k; pop the smallest whenever
    it grows past k, so the heap always holds the k largest seen so far.

    Use when: "top/smallest/largest K elements", streaming data,
    k-th largest element (peek heap[0] there).
    Time: O(n log k). Space: O(k).
    """
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)


if __name__ == "__main__":
    assert top_k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]
    print("ok")
