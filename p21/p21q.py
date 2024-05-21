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


def sum_of_proper_divisors(n: int, primes: list[int]) -> int:
    """Return sum of proper divisors of n."""
    if n < 2:
        return 0

    result, basis = 1, n
    for p in primes:
        if p > n:
            break

        if n % p == 0:
            sub_result, multiplier = 1, p
            while n and n % p == 0:
                sub_result, multiplier = sub_result + multiplier, multiplier * p
                n //= p

            result *= sub_result

    if n != 1:
        result *= 1 + n

    return result - basis


def solve(n: int) -> int:
    """Return sum of amicable numbers in [1..n] range."""
    # Time complexity: O(sqrt(n) * log(log(sqrt(n))) + n), where
    #  O(sqrt(n) * log(log(sqrt(n)))) to generate primes;
    #  O(n * sqrt(n) / log(sqrt(n))) to calculate divisor sums;
    #  O(n) to find amicable numbers.
    # Extra space complexity: O(n + sqrt(n) / log(sqrt(n))), where
    #  O(sqrt(n) / log(sqrt(n))) to hold primes;
    #  O(n) to hold divisor sums.
    primes = gen_primes(math.ceil(math.sqrt(n)) + 1)

    proper_divisor_sums = [sum_of_proper_divisors(i, primes) for i in range(n + 1)]

    def is_amicable(x: int) -> bool:
        y = proper_divisor_sums[x]
        return y <= n and y != x == proper_divisor_sums[y]

    return sum({i for i in range(2, n + 1) if is_amicable(i)})
