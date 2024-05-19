LIMIT = 4_000_000


def solve():
    """Find answer to problem 2 by directly finding all valid Fibonacci terms.

    Running time: O(LIMIT). The result comes from O(1.6 ^ N) for Fibonacci
    sequence, where N ~ log(LIMIT, base=1.6).
    Extra memory: O(1)
    """
    result, a, b = 0, 1, 2
    while b <= LIMIT:
        if b % 2 == 0:
            result += b
        a, b = b, a + b

    return result
