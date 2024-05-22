import common.generator as cg

# Upper limit was taken from https://en.wikipedia.org/wiki/Prime-counting_function.
MAX_NUMBER = 10**6
MAX_SIEVE_SIZE = (MAX_NUMBER - 1) // 2


def solve(n):
    """Return n-th (1-based) prime number below 1_000_000."""
    # Time complexity: O(n).
    # Space complexity: O(1) - a big constant is still a constant.
    if n > 78498:
        raise ValueError("n should be less than or equal to 78498.")

    for i, prime in enumerate(cg.primes(MAX_NUMBER), start=1):
        if i == n:
            return prime

    raise AssertionError("Unexpected situation.")
