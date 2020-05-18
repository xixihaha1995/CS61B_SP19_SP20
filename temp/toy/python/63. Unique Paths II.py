from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [ [0]* n for _ in range(m)]

        memo[0][0] = 1
        for i in range (m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    if i != 0 :
                        memo[i][j]  += memo[i-1][j]
                    if j != 0:
                        memo[i][j] += memo[i][j-1]
        return memo[m-1][n-1]
if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles(
        [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ))
