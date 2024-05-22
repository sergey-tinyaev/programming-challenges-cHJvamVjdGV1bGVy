def solve(n: int) -> int:
    """Return product a*b*c, where a, b and c are Pythagorean triple
    (see https://en.wikipedia.org/wiki/Pythagorean_triple) and a+b+c = n."""
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Given a system of 2 equations:
    # 1) a + b + c = n
    # 2) a^2 + b^2 = c^2
    #
    # Simplify to remove c:
    # a^2 + b^2 = (n - (a + b))^2
    #
    # Solving for b results in:
    # n^2 - 2an - 2bn + 2ab = 0 (add n^2 to both sides)
    # 2n^2 - 2an - 2bn + 2ab = n^2
    # 2n(n - a) - 2b(n - a) = n^2
    # 2(n - b)(n - a) = n^2 (simplify for b)
    # b = n - n^2 / 2(n - a) (provided that a != n, which is always the case)
    #
    # Thus, a valid *integer* solution requires n^2 to be divisible by 2(n - a).
    # Suppose q = n^2 / 2(n - a), then b = n - q, and c = q - a.
    for a in range(1, n // 3 + 1):
        q, r = divmod(n**2, 2 * (n - a))
        if r == 0:
            return a * (n - q) * (q - a)
    return -1
