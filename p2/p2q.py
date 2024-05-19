def solve():
    r, a, b = 0, 1, 2
    while b <= 4_000_000:
        if b % 2 == 0:
            r += b
        a, b = b, a + b

    return r
