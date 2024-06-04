from collections import defaultdict
import common.number as cn


def solve(k: int) -> int:
    """Return first cube whose k digit permutations are also cubes."""
    # Time: O(n) - unable to tie k to n.
    # Space: O(n) - unable to tie k to n.
    freq_map = defaultdict(set)

    x, n = 0, 0
    while True:
        x += 1
        n += 3 * x * (x - 1) + 1

        digits = tuple(sorted(cn.get_digits(n)))

        freq_map[digits].add(n)
        if len(freq_map[digits]) == k:
            return min(freq_map[digits])
