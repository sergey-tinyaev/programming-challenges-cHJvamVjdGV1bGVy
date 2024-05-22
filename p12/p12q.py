from collections import defaultdict
import math
import common.generator as cg


# Failed to approximate growth function for n based off d(n), where
# d(n) - divisor counting function. Pre-calculating primes up to 10^6 will
# helpfinding divisors for n in [1..10^12] range.
PRIMES = list(cg.primes(10**6))


def count_divisors(n: int) -> int:
    """Return number of divisors of n."""
    # Time complexity: O(n * log(log(n))) - see count_prime_freq()
    # Extra space complexity: O(n) - needed for prime sieve algorithm.
    prime_freq: dict[int, int] = defaultdict(int)
    for prime in PRIMES:
        if prime > n:
            break

        while prime <= n != 1 and n % prime == 0:
            prime_freq[prime] += 1
            n //= prime

    return math.prod((v + 1) for v in prime_freq.values())


def solve(n: int) -> int:
    """Return first triangle number with total divisor count greater than n."""
    # Time complexity:
    # Extra space complexity: O(n)
    x, dx = 0, 1
    while True:
        x, dx = x + dx, dx + 1
        if count_divisors(x) > n:
            return x
