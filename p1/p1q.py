def asum(n: int) -> int:
    """Return sum of arithmetic progression [1, 2, 3, ..., n]."""
    # Time: O(1).
    # Space: O(1).
    return n * (n + 1) // 2


def solve(n: int) -> int:
    """Return the number of number divisible by 3 or 5 in [1..n] range."""
    # Time: O(1).
    # Space: O(1).
    n -= 1
    return 3 * asum(n // 3) + 5 * asum(n // 5) - 15 * asum(n // 15)
