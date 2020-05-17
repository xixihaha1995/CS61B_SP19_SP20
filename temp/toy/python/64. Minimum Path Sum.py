from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.min = 0
        memo = [ [0] * self.n for _ in range(self.m)]
        self.dp(grid,0,0,memo)
        return self.min

    def dp(self, grid, i, j, memo):
        if( i > self.m-1 or j > self.n -1):
            return
        memo[i][j] += grid[i][j]
        if ( i == self.m-1 and j == self.n-1):
            self.min = min(self.min,memo[i][j])
            return

        self.dp(grid, i+1, j, memo)
        self.dp(grid, i, j+1, memo)


if __name__ == '__main__':
    print(Solution().minPathSum(
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
    ))
