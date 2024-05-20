def solve(n: int) -> int:
    """Return product a*b*c, where a, b and c are Pythagorean triple
    (see https://en.wikipedia.org/wiki/Pythagorean_triple) and a+b+c = n."""
    # Time complexity: O(n)
    # Space complexity: O(1)
    for a in range(1, n // 3 + 1):
        q, r = divmod(n**2, 2 * (n - a))
        if r == 0:
            return a * (n - q) * (q - a)
    return -1
