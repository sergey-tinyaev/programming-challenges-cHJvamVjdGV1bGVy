def solve(grid: list[list[int]]) -> int:
    """Return maximal path in triangular grid from top to any bottom cell."""
    # Time: O(N^2).
    # Space: O(1).
    N = len(grid)
    if N >= 2:
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[i])):
                grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])

    return grid[0][0]
