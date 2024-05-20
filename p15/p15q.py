import math


def solve(n: int) -> int:
    """Return n-th Catalan number."""
    # Time complexity: O(n + m)
    # Extra space complexity: O(1)
    return math.factorial(2 * n) // (math.factorial(n) ** 2)
