def permutations(items):
    """All orderings of items (order matters). Pick each item as the
    head, recurse on the rest.

    Use when: "all arrangements/orderings of...".
    Time: O(n!) results, O(n * n!) total work.
    """
    if len(items) <= 1:
        return [items]
    result = []
    for i, item in enumerate(items):
        rest = items[:i] + items[i + 1:]
        for perm in permutations(rest):
            result.append([item] + perm)
    return result


def combinations(items, k):
    """All size-k selections (order doesn't matter). Either skip the
    first item or take it, recurse on the rest.

    Use when: "choose k of n, order doesn't matter".
    Time: O(C(n, k)) results.
    """
    if k == 0:
        return [[]]
    if len(items) < k:
        return []
    # either skip items[0], or take it
    without_first = combinations(items[1:], k)
    with_first = [[items[0]] + c for c in combinations(items[1:], k - 1)]
    return with_first + without_first


def subsets(items):
    """Powerset: for each item, double every existing subset by
    including/excluding it.

    Use when: "all subsets/power set of...".
    Time: O(2^n) results.
    """
    result = [[]]
    for item in items:
        result += [subset + [item] for subset in result]
    return result


if __name__ == "__main__":
    assert sorted(permutations([1, 2, 3])) == sorted(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    assert sorted(combinations([1, 2, 3], 2)) == sorted([[1, 2], [1, 3], [2, 3]])
    assert sorted(subsets([1, 2])) == sorted([[], [1], [2], [1, 2]])
    print("ok")
