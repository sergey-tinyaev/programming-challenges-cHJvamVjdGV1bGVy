import common.number as cn


def is_palindrome(n: int) -> bool:
    """Return true if n is palindromic number, and false otherwise."""
    # Time: O(lg(n)).
    # Space: O(lg(n)).
    digits = cn.get_digits(n)

    return all(
        digits[i] == digits[len(digits) - 1 - i] for i in range(len(digits) // 2)
    )


def solve(n: int, m: int) -> int:
    """Return largest polyndrome that is a result of multiplication of n and m
    digit numbers."""
    # Time: O(10^(n + m) * (n + m)).
    # Space: O(n + m) - to keep a single list of maximum number of digits at any point.
    return max(
        x
        for x in (
            i * j
            for i in range(9 * 10 ** (n - 1), 10**n)
            for j in range(9 * 10 ** (m - 1), 10**m)
        )
        if is_palindrome(x)
    )
