import itertools as it


def to_int(t: tuple[int, ...]) -> int:
    """Convert tuple to number and return it."""
    # Time complexity: O(t).
    # Extra space complexity: O(1).
    result = 0
    for x in t:
        result = 10 * result + x
    return result


def solve() -> int:
    """Return 1_000_000th lexographic permutation of digits {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}."""
    # Time complexity: O(n) => O(1), cause n is fixed.
    # Extra space complexity: O(1).
    for i, p in enumerate(it.permutations(range(10), 10), start=1):
        if i == 1_000_000:
            return to_int(p)

    raise NotImplementedError("Shouldn't get here")
