from collections import defaultdict
import math


def gen_primes(n: int) -> list[int]:
    result = [2]

    sieve_size = (n - 1) // 2
    sieve = [True] * sieve_size

    for i in range(sieve_size):
        if sieve[i]:
            result.append(2 * i + 3)
            for j in range(2 * i * (i + 3) + 3, sieve_size, 2 * i + 3):
                sieve[j] = False

    return result


# I could not formulate growth function for n based off d(n), where
# d(n) - divisor counting function. Precalculating primes up to 10^6
# will allow me to calculate divisors for values up to 10^12, which
# should be sufficient.
PRIMES = gen_primes(10**6)


def count_prime_freq(n: int) -> dict[int, int]:
    # Time complexity: O(n * log(log(n)) * log(n)) - to loop over all primes up to n.
    # The upper bound is probably can be reduced further.
    # Extra space complexity: O(n) - needed for prime sieve algorithm.
    counter: dict[int, int] = defaultdict(int)
    for prime in PRIMES:
        while prime <= n and n % prime == 0:
            counter[prime] += 1
            n //= prime
        else:
            if n == 1:
                break

    return counter


def count_divisors(n: int) -> int:
    # Time complexity: O(n * log(log(n))) - see count_prime_freq()
    # Extra space complexity: O(n) - needed for prime sieve algorithm.
    return math.prod((v + 1) for v in count_prime_freq(n).values())


def solve(n: int) -> int:
    # Time complexity:
    # Extra space complexity: O(n)
    x, dx = 0, 1
    while True:
        x, dx = x + dx, dx + 1
        if count_divisors(x) > n:
            return x
