from collections import deque
import math
from typing import Generator

OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(grid: list[list[int]]) -> int:
    """Return minimal path sum from top left to bottom right while moving
    in any horizontal or vertical direction."""
    # Time: O(n*m).
    # Space: O(n*m).
    N, M = len(grid), len(grid[0])
    dp = [[math.inf] * M for _ in range(N)]

    def advance(node: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        """Return next valid points to examine."""
        i, j = node
        for di, dj in OFFSETS:
            y, x = i + di, j + dj
            if 0 <= y < N and 0 <= x < M:
                yield (y, x)

    queue = deque([((0, 0), grid[0][0])])
    while queue:
        (node, cost) = queue.popleft()
        if cost > dp[-1][-1] or cost > dp[node[0]][node[1]]:
            continue

        for y, x in advance(node):
            new_cost = grid[y][x] + cost
            if new_cost < dp[y][x]:
                queue.append(((y, x), new_cost))
                dp[y][x] = new_cost

    return int(dp[-1][-1])
