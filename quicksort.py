def quicksort(arr):
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
