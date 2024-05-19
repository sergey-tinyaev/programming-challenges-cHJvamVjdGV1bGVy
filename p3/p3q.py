import math
from typing import Generator


def gen_primes_up_to(n: int) -> Generator[int, int, None]:
    """Return a generator that yields primes up to N using Sieve of Erathothene"""

    if n >= 2:
        yield 2

        N = (n - 1) // 2
        sieve = [True] * N
        for i in range(N):
            if sieve[i]:
                yield 2 * i + 3

                for j in range(2 * i * (i + 3) + 3, N, 2 * i + 3):
                    sieve[j] = False


def solve(n: int) -> int:
    """Return the highest prime factor of N."""

    # Running time analysis: O(N * log(log(N)) + sqrt(N) / ln(N)), where
    #   N * log(log(N)) - is runtime asymptotic to generate primes,
    #   sqrt(N) / ln(N) - the number of prime factors less than or equal N.
    #
    # Extra Space analysis: O(sqrt(N))
    #   used by underlying sieve algorithm to generate primes.
    upper_bound_for_factor = math.ceil(math.sqrt(n)) + 1
    for prime_factor in gen_primes_up_to(upper_bound_for_factor):
        if prime_factor > n:
            break
        if n % prime_factor == 0:
            n //= prime_factor
            result = prime_factor
    else:
        result = n

    return result
