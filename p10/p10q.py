def solve(n):
    """Return sum of all primes below n."""
    # Time complexity: O(n*log(log(n)))
    # Extra space complexity: O(n)
    if n < 2:
        return 0

    result = 2

    # See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    sieve_size = (n - 1) // 2
    sieve = [True] * sieve_size

    for i in range(sieve_size):
        if sieve[i]:
            result += 2 * i + 3
            for j in range(2 * i * (i + 3) + 3, sieve_size, 2 * i + 3):
                sieve[j] = False

    return result
