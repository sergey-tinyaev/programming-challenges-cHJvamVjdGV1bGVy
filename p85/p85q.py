import math


def count_rectangles(n, m):
    """Return total number of rectangles in n x m grid."""
    # Time: O(1).
    # Space: O(1).
    return n * m * (n + 1) * (m + 1) // 4


def solve(n: int) -> int:
    """Return area of the grid with number of rectangles closest to n."""
    # Time: O(n).
    # Space: O(1).
    r = 1 + math.ceil(math.sqrt(n)) if n > 100 else n
    return min(
        (abs(count_rectangles(i, j) - n), i * j)
        for i in range(1, r + 1)
        for j in range(1, r + 1)
    )[1]
