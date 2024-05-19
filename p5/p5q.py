import math


def solve(n):
    """Return the least common multiple for arithmetic progression [1, 2, 3, ..., n]."""
    # Time complexity: O(N * log(N))
    # Space complexity: O(log(N)) - couldn't find space complexity analysis
    # for math.lcm() function in Python's standard library. It is either O(1)
    # for iterative solution or O(log(N)) for recursive solution.
    return math.lcm(*range(2, n + 1))
