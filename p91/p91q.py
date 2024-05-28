import math


def solve(n: int) -> int:
    """Return the number of right triangles in 0 <= x1,y1,x2,y2 <= n range."""
    # Time: O(n^2).
    # Space: O(1).
    result = 3 * n**2

    for x1 in range(1, n + 1):
        for y1 in range(1, n + 1):
            g = math.gcd(x1, y1)
            dx, dy = x1 // g, y1 // g

            result += min(y1 // dx, (n - x1) // dy)
            result += min(x1 // dy, (n - y1) // dx)

    return result
