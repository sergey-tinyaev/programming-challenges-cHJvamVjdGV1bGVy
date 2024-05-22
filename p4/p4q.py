import common.number as cn


def is_palindrome(n: int) -> bool:
    """Return true if n is palindromic number, and false otherwise."""
    # Runtime analysis: O(lg(n))
    # Extra space: O(lg(n)) - to hold digits in a list
    digits = cn.get_digits(n)

    return all(
        digits[i] == digits[len(digits) - 1 - i] for i in range(len(digits) // 2)
    )


def solve(n, m):
    """Return largest polyndrome that is a result of multiplication of n and m
    digit numbers."""
    # Runtime analysis: O(10**(n + m) * (n + m))
    # Extra space: O(10**(n + m)) - to hold intermediate list of
    return max(
        x
        for x in (
            i * j
            for i in range(9 * 10 ** (n - 1), 10**n)
            for j in range(9 * 10 ** (m - 1), 10**m)
        )
        if is_palindrome(x)
    )
