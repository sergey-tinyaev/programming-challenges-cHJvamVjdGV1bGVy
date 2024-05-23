def solve(n: int) -> int:
    """Return sum of numbers on diagonals of n x n spiral."""
    # Time: O(n).
    # Space: O(1).
    if n % 2 == 0:
        raise ValueError("n must be odd.")
    n //= 2

    result = 1

    if n != 0:
        value, step = 1, 2

        for _ in range(n):
            result += 4 * value + 10 * step
            value += 4 * step
            step += 2

    return result
