def solve(numbers: list[str]) -> int:
    """Return sum of numbers."""
    # Time: O(n).
    # Space: O(1).
    return sum(map(int, numbers))
