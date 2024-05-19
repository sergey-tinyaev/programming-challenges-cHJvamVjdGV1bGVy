# Upper limit was taken from https://en.wikipedia.org/wiki/Prime-counting_function.
MAX_PRIMES = 10**6


def solve(n):
    if n == 1:
        return 2

    x, sieve = 1, [True] * MAX_PRIMES
    for i in range(MAX_PRIMES):
        if sieve[i]:
            x += 1
            if x == n:
                return 2 * i + 3

            for j in range(2 * i * (i + 3) + 3, MAX_PRIMES, 2 * i + 3):
                sieve[j] = False

    raise ValueError("the value is out of range")
