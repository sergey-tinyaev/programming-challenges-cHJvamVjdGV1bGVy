def solve(grid: list[list[int]]) -> int:
    """Return minimal path sum from left to right column."""
    # Time: O(n^m).
    # Space: O(n).
    N, M = len(grid), len(grid[0])

    col = [0] * N
    for j in range(M - 2, -1, -1):
        col[0] = grid[0][j] + grid[0][j + 1]
        for i in range(1, N):
            col[i] = grid[i][j] + min(col[i - 1], grid[i][j + 1])

        col[N - 1] = min(col[N - 1], grid[N - 1][j] + grid[N - 1][j + 1])
        for i in range(N - 2, -1, -1):
            col[i] = min(col[i], grid[i][j] + col[i + 1])

        for i in range(N):
            grid[i][j] = col[i]

    return min(grid[i][0] for i in range(N))
