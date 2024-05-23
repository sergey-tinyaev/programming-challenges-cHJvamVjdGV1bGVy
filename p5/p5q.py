import math


def solve(n: int) -> int:
    """Return the least common multiple for arithmetic progression [1, 2, 3, ..., n]."""
    # Time: O(n * max(a, b)) - optimal lcm() implementation.
    # Space: O(max(a, b)) - optimal lcm() implementation.
    return math.lcm(*range(2, n + 1))
