def binary_search(arr, target):
    """Binary search: halve the search space on a sorted array.

    Use when: array is sorted, or you can binary-search an answer
    (monotonic predicate) instead of a value directly.
    Time: O(log n). Space: O(1).
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 11) == 5
    assert binary_search(arr, 4) == -1
    print("ok")
