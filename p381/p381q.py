import common.generator as cg


def solve(n):
    primes = cg.primes(n)
    next(primes)  # skip 2
    next(primes)  # skip 3

    return sum(-3 * (1 + p // 2) ** 3 % p for p in primes)
