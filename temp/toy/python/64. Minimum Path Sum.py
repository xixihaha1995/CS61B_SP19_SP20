from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i == j == 0):
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                    continue
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]


if __name__ == '__main__':
    print(Solution().minPathSum(
        [[1, 2, 5], [3, 2, 1]]
    ))
