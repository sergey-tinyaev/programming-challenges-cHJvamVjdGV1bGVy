BASIS = ord("A") - 1


def alpha_sum(s: str) -> int:
    """Return alphabetical value of s."""
    # Time complexity: O(s).
    # Extra space complexity: O(1).
    return sum(ord(ch) - BASIS for ch in s)


def solve(xs):
    """Return total score of xs."""
    # Time complexity: O(n*log(n) + n*s).
    # Extra space complexity: O(1).
    xs.sort()
    return sum(i * alpha_sum(s) for i, s in enumerate(xs, start=1))
