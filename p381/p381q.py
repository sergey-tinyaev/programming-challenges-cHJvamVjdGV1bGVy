import common.generator as cg


def solve(n: int) -> int:
    """Return sum of ((p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)!) % p for all primes
    below n."""
    # Time: O(n*log(log(n))).
    # Space: O(n).
    primes = cg.primes(n)
    next(primes)  # skip 2
    next(primes)  # skip 3

    return sum(-3 * (1 + p // 2) ** 3 % p for p in primes)
