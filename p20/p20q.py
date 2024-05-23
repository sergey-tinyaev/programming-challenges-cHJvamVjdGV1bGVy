import math
import common.number as cn


def solve(n: int) -> int:
    """Return sum of digits of n!."""
    # Time: O(n + lg(n!)) => O(n + n*log(n)) => O(n*log(n)).
    # Space: O(1).
    return cn.sum_of_digits(math.factorial(n))
