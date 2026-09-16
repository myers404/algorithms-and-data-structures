def permutations(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i, item in enumerate(items):
        rest = items[:i] + items[i + 1:]
        for perm in permutations(rest):
            result.append([item] + perm)
    return result


def combinations(items, k):
    if k == 0:
        return [[]]
    if len(items) < k:
        return []
    # either skip items[0], or take it
    without_first = combinations(items[1:], k)
    with_first = [[items[0]] + c for c in combinations(items[1:], k - 1)]
    return with_first + without_first


def subsets(items):
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
