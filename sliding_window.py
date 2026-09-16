def sliding_window(arr, k):
    """Fixed-size sliding window: maintain a running aggregate over a
    window of size k, add the entering element and remove the leaving one.

    Use when: "max/min/sum of every subarray of size k".
    Time: O(n). Space: O(1).
    """
    window_sum = sum(arr[:k])
    best = window_sum
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        best = max(best, window_sum)
    return best


def variable_window(arr, limit):
    """Variable-size sliding window: grow the right edge; while the
    window violates a constraint, shrink from the left.

    Use when: "longest/shortest subarray/substring satisfying X"
    (sum <= limit, at most K distinct chars, no repeats, etc).
    Time: O(n) — each pointer moves forward only. Space: O(1) or O(k).
    """
    left = 0
    total = 0
    best = 0
    for right in range(len(arr)):
        total += arr[right]
        while total > limit:
            total -= arr[left]
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert sliding_window([1, 4, 2, 10, 2, 3, 1], 3) == 16
    assert variable_window([1, 2, 1, 0, 1, 1, 0], 4) == 5
    print("ok")
