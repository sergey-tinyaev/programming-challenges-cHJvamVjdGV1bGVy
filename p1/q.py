def asum(n):
    """Return sum of arithmetic progression [1, 2, 3, ..., n]."""
    return n * (n + 1) // 2


def solve(n):
    """Find answer to problem 1 using arithmetic sum formula.

    Running time: O(1)
    Extra memory: O(1)
    """
    n -= 1
    return 3 * asum(n // 3) + 5 * asum(n // 5) - 15 * asum(n // 15)
