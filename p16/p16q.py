def sum_of_digits(n: int) -> int:
    """Return sum of digits of n."""
    # Time complexity: O(lg(n))
    # Extra space complexity: O(1)
    result = 0
    while n:
        n, digit = divmod(n, 10)
        result += digit
    return result


def solve(n: int) -> int:
    """Return sum of digits of 2^n."""
    # Time complexity: O(lg(2^n)) => O(n * lg(2)) => O(n)
    # Extra space complexity: O(1)
    return sum_of_digits(2**n)
