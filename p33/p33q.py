import math


def solve() -> int:
    """Return denominator of the product of all digit-cancelling fractions in
    lowest common terms."""
    # Time: O(9^3).
    # Space: O(1).
    num, denom = 1, 1

    for a in range(1, 10):
        for b in range(a, 10):
            ab = 10 * a + b
            for c in range(10):
                bc = 10 * b + c
                if ab != bc and ab * c == bc * a:
                    num *= a
                    denom *= c

    return denom // math.gcd(num, denom)
