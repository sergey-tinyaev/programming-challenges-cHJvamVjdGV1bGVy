def solve(numbers: list[str]) -> str:
    """Return sum of numbers."""
    # Time: O(n).
    # Space: O(1).
    result = sum(map(int, numbers))
    return str(result)[:10]
