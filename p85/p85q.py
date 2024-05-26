def solve(n: int) -> int:
    """Return area of the grid with number of rectangles closest to n."""
    # Time: O(sqrt(n)).
    # Space: O(1).

    i = j = x = 1
    min_diff, result = n - 1, 1

    while x < n:
        j += 1
        x += j

    diff = x - n
    if diff < min_diff:
        min_diff, result = diff, i * j

    diff = n + j - x
    if diff < min_diff:
        min_diff, result = diff, i * (j - 1)

    if min_diff == 0:
        return result

    m = 1
    while j > 1:
        i += 1
        m += i
        x = m * x // (m - i)

        while x > n:
            x -= m * j
            j -= 1

        diff = n - x
        if diff < min_diff:
            min_diff, result = diff, i * j

        diff = x + m * (j + 1) - n
        if diff < min_diff:
            min_diff, result = diff, i * (j + 1)

        if min_diff == 0:
            return result

    return result
