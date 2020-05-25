class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        data = []
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    data.append(i,j,0)
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        while data:
            i, j , res = data.pop(0)
            for xd, yd in d:
                x, y = i + xd, j + yd
                if 0 <= x < r and 0 <= y < c and not grid[i][j]:
                    grid[i][j] = 1
                    data.append(i,j, res + 1)
        return res if res !=0 else -1

