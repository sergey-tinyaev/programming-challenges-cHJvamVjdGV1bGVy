def solve(n: int, k: int) -> int:
    """Return sum of nodes in path from root to target node in rooted trees."""
    # Time: O(log(n-k)).
    # Space: O(1).
    diff, result, power = n - k, n, 1
    while diff:
        diff, is_on_path = divmod(diff, 2)
        if is_on_path:
            n -= power
            result += n
        power <<= 1
    return result
