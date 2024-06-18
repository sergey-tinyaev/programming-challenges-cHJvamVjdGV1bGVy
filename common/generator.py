from typing import Generator


def primes(upper_bound: int) -> Generator[int, None, None]:
    """Return primes up to (and including) upper_bound."""
    # Time: O(n*log(log(n))).
    # Space: O(n).
    if upper_bound >= 2:
        yield 2

        if upper_bound > 2:
            # See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
            sieve_size = (upper_bound - 1) // 2
            sieve = [True] * sieve_size
            for i in range(sieve_size):
                if sieve[i]:
                    yield 2 * i + 3
                    for j in range(2 * i * (i + 3) + 3, sieve_size, 2 * i + 3):
                        sieve[j] = False
