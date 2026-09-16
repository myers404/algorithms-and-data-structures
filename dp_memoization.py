from functools import lru_cache


def fib(n):
    """Top-down memoization: write the naive recursive solution first,
    then cache results keyed on the recursive call's arguments.

    Use when: overlapping subproblems + optimal substructure
    ("count the ways", "min/max cost to..."). Easier to derive than
    bottom-up: solve the brute-force recursion, then add @lru_cache
    (or a manual dict) once it's correct.
    Time/space: O(distinct subproblems).
    """
    @lru_cache(maxsize=None)
    def helper(i):
        if i <= 1:
            return i
        return helper(i - 1) + helper(i - 2)

    return helper(n)


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    print("ok")
