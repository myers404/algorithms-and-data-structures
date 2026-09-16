def quicksort(arr):
    """Quicksort: pick a pivot, partition into less/equal/greater, recurse.

    Use when: general-purpose sort, in-place variants save space over
    mergesort. Know it for "explain quickselect" (same partition, only
    recurse into the side containing the target index) e.g. kth largest.
    Time: O(n log n) average, O(n^2) worst case. Space: O(n) here
    (this version isn't in-place, for readability).
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)


if __name__ == "__main__":
    assert quicksort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    print("ok")
