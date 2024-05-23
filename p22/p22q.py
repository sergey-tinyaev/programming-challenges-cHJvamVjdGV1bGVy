BASIS = ord("A") - 1


def alpha_sum(s: str) -> int:
    """Return alphabetical value of s."""
    # Time: O(s).
    # Space: O(1).
    return sum(ord(ch) - BASIS for ch in s)


def solve(xs: list[str]):
    """Return total score of xs."""
    # Time: O(n*log(n) + n*s).
    # Space: O(1).
    xs.sort()
    return sum(i * alpha_sum(s) for i, s in enumerate(xs, start=1))
