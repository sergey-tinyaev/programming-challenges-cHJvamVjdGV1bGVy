def is_palindrome(n: int) -> bool:
    digits = []

    if n == 0:
        digits = [0]
    else:
        while n:
            n, digit = divmod(n, 10)
            digits.append(digit)

    return all(
        digits[i] == digits[len(digits) - 1 - i] for i in range(len(digits) // 2)
    )


def solve(n, m):
    return max(
        x
        for x in (
            i * j
            for i in range(9 * 10 ** (n - 1), 10**n)
            for j in range(9 * 10 ** (m - 1), 10**m)
        )
        if is_palindrome(x)
    )
