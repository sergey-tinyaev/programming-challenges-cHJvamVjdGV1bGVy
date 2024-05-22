def get_digits(n: int) -> list[int]:
    """Return digits of n as list."""
    # Time: O(lg(n)).
    # Space: O(lg(n)).
    if n < 10:
        return [n]

    result = []

    while n != 0:
        n, digit = divmod(n, 10)
        result.append(digit)

    result.reverse()

    return result


def sum_of_digits(n: int) -> int:
    """Return sum of digits of n."""
    # Time: O(lg(n))
    # Space: O(1)
    result = 0

    while n != 0:
        n, digit = divmod(n, 10)
        result += digit

    return result
