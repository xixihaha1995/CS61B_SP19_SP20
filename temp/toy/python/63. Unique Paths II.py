from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [ [0]* n for _ in range(m)]

        return self.dfs(obstacleGrid, m-1, n-1, memo)

    def dfs(self, obstacleGrid, i, j, memo):

        if obstacleGrid[i][j] == 1:
            return 0
        if i <0 or j < 0:
            return 0
        if i == j == 0:
            return 1
        if memo[i][j]:
            return memo[i][j]
        up = self.dfs(obstacleGrid, i-1, j, memo)
        left = self.dfs(obstacleGrid, i, j-1, memo)
        memo[i][j] = up + left
        return memo[i][j]
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     memo = [[0] * n for _ in range(m)]
    #     return self.dfs(m - 1, n - 1, obstacleGrid, memo)
    #
    # def dfs(self, m, n, obstacleGrid, memo):  # methods of postion m, n
    #     if obstacleGrid[m][n] == 1:
    #         return 0
    #     if m < 0 or n < 0:
    #         return 0
    #     if m == n == 0:
    #         return 1
    #     if memo[m][n]:
    #         return memo[m][n]
    #     up = self.dfs(m - 1, n, obstacleGrid, memo)
    #     left = self.dfs(m, n - 1, obstacleGrid, memo)
    #     memo[m][n] = up + left
    #     return memo[m][n]

if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ))
