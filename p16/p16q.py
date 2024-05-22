import common.number as cn


def solve(n: int) -> int:
    """Return sum of digits of 2^n."""
    # Time complexity: O(lg(2^n)) => O(n * lg(2)) => O(n)
    # Extra space complexity: O(1)
    return cn.sum_of_digits(2**n)
