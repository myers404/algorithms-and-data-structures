def backtrack(candidates, is_valid, is_complete):
    """Backtracking: choose -> explore -> unchoose.

    Use when: building all valid sequences/subsets under constraints
    (permutations, N-Queens, combination sum, Sudoku). Recognize by:
    "find all ways to..." / "generate all valid...".
    Time: O(branches^depth) in the worst case, pruned by is_valid.
    """
    results = []
    path = []

    def helper():
        if is_complete(path):
            results.append(path[:])
            return
        for choice in candidates:
            if is_valid(path, choice):
                path.append(choice)
                helper()
                path.pop()

    helper()
    return results


if __name__ == "__main__":
    # example: all sequences of length 2 from [1, 2, 3] with no repeats
    results = backtrack(
        candidates=[1, 2, 3],
        is_valid=lambda path, choice: choice not in path,
        is_complete=lambda path: len(path) == 2,
    )
    assert sorted(results) == sorted(
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
    )
    print("ok")
