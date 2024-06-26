import common.generator as cg

# Upper limit was taken from https://en.wikipedia.org/wiki/Prime-counting_function.
MAX_NUMBER = 10**6


def solve(n: int) -> int:
    """Return n-th (1-based) prime number below 1_000_000."""
    # Time complexity: O(n).
    # Space complexity: O(MAX_NUMBER) - to generate primes.
    if n > 78498:
        raise ValueError("n should be less than or equal to 78498.")

    for i, prime in enumerate(cg.primes(MAX_NUMBER), start=1):
        if i == n:
            return prime

    raise AssertionError("Unexpected situation.")
