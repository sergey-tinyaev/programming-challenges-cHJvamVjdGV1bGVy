def solve(n):
    """Return the difference between square of sum of arithmetic progression [1, 2, 3,
    ..., n] and sum of squares of elements of arithmetic progression [1, 2, 3, ..., n].
    """
    # Time complexity: O(1)
    # Space complexity: O(1)

    # https://en.wikipedia.org/wiki/Triangular_number
    square_of_sum = (n * (n + 1) // 2) ** 2

    # https://en.wikipedia.org/wiki/Square_pyramidal_number
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

    return square_of_sum - sum_of_squares
