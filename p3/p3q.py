import math
import common.generator as cg


def solve(n: int) -> int:
    """Return the greatest prime factor of n."""

    # Time: O(sqrt(n) * log(log(n)) + sqrt(n) / ln(n)), where
    #   O(sqrt(n) * log(log(n))) - to generate primes;
    #   O(sqrt(n) / ln(n)) - to iterate over prime factors less than or equal sqrt(n).
    #
    # Space: O(sqrt(n)) - used by sieve to generate primes.
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
