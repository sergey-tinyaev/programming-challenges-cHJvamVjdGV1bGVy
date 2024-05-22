import common.generator as cg


def solve(n):
    """Return sum of all primes below n."""
    # Time complexity: O(n*log(log(n))).
    # Extra space complexity: O(n).
    return sum(cg.primes(n))
