from collections import deque


def solve() -> int:
    """Return P(a) from {P_a, P_b, P_c, P_d} set, where  P_a, P_b, P_c and P_d
    are pentagonal numbers, and P_a = P_c - P_b and P_d = P_c + P_b."""
    # Time: O(n^2).
    # Space: O(n).
    pentagonals = {1}
    candidates: deque[int] = deque()

    n, p = 1, 1
    while True:
        for candidate in candidates:
            if (p - candidate) in pentagonals and (2 * candidate - p) in pentagonals:
                return 2 * candidate - p

        candidates.append(p)

        n, p = n + 1, p + 3 * n + 1
        pentagonals.add(p)

        while candidates and 2 * candidates[0] < p:
            candidates.popleft()
