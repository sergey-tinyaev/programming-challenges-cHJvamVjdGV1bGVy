import math
import common.generator as cg


def solve(n: int) -> int:
    """Return the highest prime factor of N."""

    # Running time analysis: O(N * log(log(N)) + sqrt(N) / ln(N)), where
    #   N * log(log(N)) - is runtime asymptotic to generate primes,
    #   sqrt(N) / ln(N) - the number of prime factors less than or equal N.
    #
    # Extra Space analysis: O(sqrt(N))
    #   used by underlying sieve algorithm to generate primes.
    upper_bound_for_factor = math.ceil(math.sqrt(n)) + 1
    for prime_factor in cg.primes(upper_bound_for_factor):
        if prime_factor > n:
            break
        if n % prime_factor == 0:
            n //= prime_factor
            result = prime_factor
    else:
        result = n

    return result
