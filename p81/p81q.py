def solve(grid: list[list[int]]) -> int:
    """Return minimal path sum from top left to bottom right by only moving
    down and right in given grid."""
    # Time: O(n^2).
    # Space: O(n^2).
    N, M = len(grid), len(grid[0])

    for i in range(N - 2, -1, -1):
        grid[i][M - 1] += grid[i + 1][M - 1]

    for j in range(M - 2, -1, -1):
        grid[N - 1][j] += grid[N - 1][j + 1]

    for i in range(N - 2, -1, -1):
        for j in range(M - 2, -1, -1):
            grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

    return grid[0][0]
