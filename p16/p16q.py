import common.number as cn


def solve(n: int) -> int:
    """Return sum of digits of 2^n."""
    # Time: O(n).
    # Space: O(1).
    return cn.sum_of_digits(2**n)
