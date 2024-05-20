def solve(grid: list[list[int]]) -> int:
    """Returns greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in provided grid."""
    # Time complexity: O(N * M * T)
    # Extra space complexity: O(1)
    N, M, T = len(grid), len(grid[0]), 4

    result = 0

    for i in range(N):
        for j in range(M):
            # LEFT -> RIGHT
            if 0 <= i < N and 0 <= j < M - T:
                r = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
                if r > result:
                    result = r

            # UP -> DOWN
            if 0 <= i < N - T and 0 <= j < M:
                r = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
                if r > result:
                    result = r

            # UP_LEFT -> DOWN_RIGHT
            if 0 <= i < N - T and 0 <= j < M - T:
                r = (
                    grid[i][j]
                    * grid[i + 1][j + 1]
                    * grid[i + 2][j + 2]
                    * grid[i + 3][j + 3]
                )
                if r > result:
                    result = r

            # DOWN_LEFT -> UP_RIGHT
            if T - 1 <= i < N and 0 <= j < M - T:
                r = (
                    grid[i][j]
                    * grid[i - 1][j + 1]
                    * grid[i - 2][j + 2]
                    * grid[i - 3][j + 3]
                )
                if r > result:
                    result = r

    return result
