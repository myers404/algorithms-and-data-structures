def two_pointers(arr, target):
    """Two pointers converging from both ends of a sorted array.

    Use when: "pair/triplet in sorted array summing to X", palindrome
    checks, removing duplicates in place, container-with-most-water.
    Time: O(n). Space: O(1).
    """
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        total = arr[lo] + arr[hi]
        if total == target:
            return (lo, hi)
        if total < target:
            lo += 1
        else:
            hi -= 1
    return None


if __name__ == "__main__":
    assert two_pointers([1, 2, 3, 5, 8], 10) == (1, 4)
    assert two_pointers([1, 2, 3], 100) is None
    print("ok")
