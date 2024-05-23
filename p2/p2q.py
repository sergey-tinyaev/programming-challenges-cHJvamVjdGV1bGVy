LIMIT = 4_000_000


def solve() -> int:
    """Return sum of even Fibonacci terms no greater than n."""
    # Time: O(LIMIT).
    # Space: O(1).
    result, a, b = 0, 1, 2
    while b <= LIMIT:
        if b % 2 == 0:
            result += b
        a, b = b, a + b

    return result
