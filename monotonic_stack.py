def next_greater(arr):
    """Monotonic stack: keep indices whose answer isn't known yet, in
    increasing (or decreasing) value order; pop and resolve when a
    value breaks the order.

    Use when: "next greater/smaller element", daily temperatures,
    largest rectangle in histogram, stock span.
    Time: O(n) — each index pushed/popped once. Space: O(n).
    """
    result = [-1] * len(arr)
    stack = []  # indices with no greater element found yet
    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] < val:
            result[stack.pop()] = i
        stack.append(i)
    return result


if __name__ == "__main__":
    assert next_greater([2, 1, 3, 4, 1]) == [2, 2, 3, -1, -1]
    print("ok")
