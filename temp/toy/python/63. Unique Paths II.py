from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]* n for _ in range(m) ]
        if obstacleGrid[0][0] == 0:
            dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i != 0: dp[i][j] += dp[i-1][j]
                    if j != 0: dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles(
        [[1,0]]
    ))
