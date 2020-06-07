import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        q = collections.deque([])
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if self.island(grid, i, j):
                    res += 1
        return res
    def island(self,grid, i, j):
        if 0<= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                self.island(grid, x,y)
            return True

if __name__ == '__main__':
    print(Solution().numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ))