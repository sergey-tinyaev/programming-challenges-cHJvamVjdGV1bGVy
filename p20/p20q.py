import math


def sum_of_digits(n: int) -> int:
    """Return sum of digits of n."""
    # Time complexity: O(lg(n)).
    # Extra space complexity: O(1).
    result = 0
    while n != 0:
        n, digit = divmod(n, 10)
        result += digit
    return result


def solve(n: int) -> int:
    """Return sum of digits of n!."""
    # Time complexity: O(n + lg(n!)) => O(n + n*log(n)) => O(n*log(n)).
    # Extra space complexity: O(1).
    return sum_of_digits(math.factorial(n))
