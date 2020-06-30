class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j, grid, newnumber):
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = newnumber
            return 1 + dfs(i-1, j, grid, newnumber) + dfs(i, j-1, grid, newnumber) + dfs(i+1, j, grid, newnumber) + dfs(i, j+1, grid, newnumber)
        m = len(grid)
        n = len(grid[0])
        newnumber = 1
        area = {}
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    newnumber += 1
                    area[newnumber] = dfs(i, j, grid, newnumber)
                    maxarea = max(maxarea, area[newnumber])
        maxareas = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    areas = 1
                    res = []
                    if i+1 < m:
                        res.append(grid[i+1][j])
                    if i - 1 >= 0:
                        res.append(grid[i-1][j])
                    if j + 1 < n:
                        res.append(grid[i][j+1])
                    if j - 1 >= 0:
                        res.append(grid[i][j-1])
                    res = list(set(res))
                    for k in range(len(res)):
                        areas += area.get(res[k], 0)
                    maxareas = max(maxareas, areas)
        return max(maxareas, maxarea)