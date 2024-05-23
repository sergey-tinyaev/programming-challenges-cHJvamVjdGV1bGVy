from collections import defaultdict
import math
import common.generator as cg


def count_divisors(n: int, primes: list[int]) -> int:
    """Return number of divisors of n."""
    # Time: O(p * log(n)), where p = len(primes).
    # Space: O(p).
    prime_freq: dict[int, int] = defaultdict(int)
    for prime in primes:
        if prime > n:
            break

        while prime <= n != 1 and n % prime == 0:
            prime_freq[prime] += 1
            n //= prime

    return math.prod((v + 1) for v in prime_freq.values())


def solve(n: int) -> int:
    """Return first triangle number with total divisor count greater than n."""
    # Time:
    # Space: O(n)

    # Failed to approximate growth function for n based off d(n), where
    # d(n) - divisor counting function. Pre-calculating primes up to 10^6 will
    # helpfinding divisors for n in [1..10^12] range.
    primes = list(cg.primes(10**6))

    x, dx = 0, 1
    while True:
        x, dx = x + dx, dx + 1
        if count_divisors(x, primes) > n:
            return x
