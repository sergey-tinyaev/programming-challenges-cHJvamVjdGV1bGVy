import math


def solve(n: int) -> int:
    """Return n-th Catalan number."""
    # Time: O(n).
    # Space: O(1).
    return math.factorial(2 * n) // (math.factorial(n) ** 2)
