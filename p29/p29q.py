def solve(n: int) -> int:
    """Return a number of unique numbers a^b, where a in [2..n] and b in [2..n]."""
    # Time: O(n^2).
    # Space: O(n^2).
    return len({a**b for a in range(2, n + 1) for b in range(2, n + 1)})
