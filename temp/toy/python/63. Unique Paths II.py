class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [ [0]* len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.dfs(obstacleGrid, m-1, n-1, memo)
    def dfs(self, obstacleGrid, i, j, memo):
        if obstacleGrid[i][j] == 1:
            return 0
        if i <0 or j < 0:
            return 0
        if obstacleGrid[i][j]:
            return obstacleGrid[i][j]
        up = self.dfs(obstacleGrid, i-1, j, memo)
        left = self.dfs(obstacleGrid, i, j-1, memo)
        memo[i][j] = up + left

if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ))
