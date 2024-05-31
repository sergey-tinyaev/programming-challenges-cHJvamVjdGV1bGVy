def solve(n):
    """Return number of entries of first n rows of Pascal's triangle
    not divisible by 7."""
    # Time: O(log7(n)).
    # Space: O(1).

    i = sub_sum = 1
    while 7 * i < n:
        i, sub_sum = i * 7, sub_sum * 28

    result, total_mult = 0, 1
    while n:
        full_rows, n = divmod(n, i)

        result += total_mult * sub_sum * full_rows * (full_rows + 1) // 2
        total_mult *= 1 + full_rows

        i, sub_sum = i // 7, sub_sum // 28

    return result
