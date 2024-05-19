def solve(n):
    """Return the difference between square of sum of arithmetic progression [1, 2, 3, ..., n]
    and sum of squares of elements of arithmetic progression [1, 2, 3, ..., n]."""
    # Time complexity: O(1)
    # Space complexity: O(1)
    return (n * (n + 1) // 2) ** 2 - n * (n + 1) * (2 * n + 1) // 6
