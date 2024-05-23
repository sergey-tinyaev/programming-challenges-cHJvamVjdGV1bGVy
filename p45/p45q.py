def solve(n: int) -> int:
    """Return n-th (1-based) number that is triangular, pentagonal and hexagonal."""
    # Time: O(?).
    # Space: O(1).

    # Every hexagonal number is also triangular, so there is no need
    # to deal with triangular numbers at all.
    P = H = 1
    Pn = Hn = 1

    c = 0
    while c < n:
        if P < H:
            Pn += 1
            P += 3 * Pn - 2
        else:
            Hn += 1
            H += 4 * Hn - 3

        if P == H:
            c += 1

    return P
