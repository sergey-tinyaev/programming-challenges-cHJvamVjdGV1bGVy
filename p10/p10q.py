import common.generator as cg


def solve(n):
    """Return sum of all primes below n."""
    # Time: O(n*log(log(n))).
    # Space: O(n).
    return sum(cg.primes(n))
