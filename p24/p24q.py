import itertools as it


def to_int(t: tuple[int, ...]) -> int:
    """Convert tuple to number and return it."""
    # Time: O(t).
    # Space: O(1).
    result = 0
    for x in t:
        result = 10 * result + x
    return result


def solve(n: int) -> int:
    """Return 1_000_000th lexographic permutation of digits {0, 1, 2, 3, 4, 5,
    6, 7, 8, 9}."""
    # Time: O(n).
    # Space: O(1).
    if n == 0:
        raise ValueError("n must be > 0.")

    for i, p in enumerate(it.permutations(range(10), 10), start=1):
        if i == n:
            return to_int(p)

    raise NotImplementedError("Shouldn't get here")
