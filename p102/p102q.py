def identify_plane_side(x1: int, y1: int, x2: int, y2: int) -> bool:
    """Return True if origin is on the left side of given vector,
    and False otherwise."""
    # Time: O(1).
    # Space: O(1).
    return x2 * y1 > x1 * y2


def is_origin_inside_triangle(
    triangle: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]
) -> bool:
    """Return if origin is inside the triangle."""
    # Time: O(1).
    # Space: O(1).
    (xa, ya), (xb, yb), (xc, yc) = triangle
    return (
        identify_plane_side(xa, ya, xb, yb)
        == identify_plane_side(xb, yb, xc, yc)
        == identify_plane_side(xc, yc, xa, ya)
    )


def solve(
    triangles: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]
) -> int:
    """Return how many triangles contain origin."""
    # Time: O(n).
    # Space: O(1).
    return sum(1 for triangle in triangles if is_origin_inside_triangle(triangle))
