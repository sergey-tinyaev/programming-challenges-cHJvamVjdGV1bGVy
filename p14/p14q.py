def advance(x: int) -> int:
    """Return next element in Collatz sequence."""
    # Time complexity: O(1)
    # Extra space complexity: O(1)
    return (x // 2) if x % 2 == 0 else (3 * x + 1)


def walk(x: int, cache: dict[int, int]) -> int:
    """Return length of Collatz chain for a given starting number."""
    # Time complexity: O(?) - unable to correctly deduce complexity.
    # Extra space complexity: O(?) - unable to correctly deduce complexity.
    if x not in cache:
        cache[x] = 1 + walk(advance(x), cache)
    return cache[x]


def solve(n: int) -> int:
    """Return starting number in [1..n] range that produces the longest
    Collatz chain."""
    # Time complexity: O(n * ?) - unable to correctly deduce complexity.
    # Extra space complexity: O(?) - unable to correctly deduce complexity.
    cache = {1: 1}

    max_chain_count, result = 1, 1
    for number in range(2, n + 1):
        chain_count = walk(number, cache)
        if chain_count > max_chain_count:
            max_chain_count, result = chain_count, number

    return result
