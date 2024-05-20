# Upper limit was taken from https://en.wikipedia.org/wiki/Prime-counting_function.
MAX_NUMBER = 10**6
MAX_SIEVE_SIZE = (MAX_NUMBER - 1) // 2


def solve(n):
    """Return n-th prime number below 1_000_000."""
    # Time complexity: O(n).
    # Space complexity: O(1) - a big constant is still a constant.
    if n == 1:
        return 2

    if n > 78498:
        raise ValueError("n should be less than or equal to 78498.")

    # See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    x, sieve = 1, [True] * MAX_SIEVE_SIZE
    for i in range(MAX_SIEVE_SIZE):
        if sieve[i]:
            x += 1
            if x == n:
                return 2 * i + 3
            for j in range(2 * i * (i + 3) + 3, MAX_SIEVE_SIZE, 2 * i + 3):
                sieve[j] = False
