class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        maxLen = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                    curlen = maxLen
                    while i + curlen < m and j + curlen < n:
                        flag2 = True
                        for a in range(i, i+curlen+1):
                            if grid[a][j] != 1:
                                flag1 = False
                                break
                        if not flag1: break
                        for b in range(j, j + curlen + 1):
                            if grid[i][b] != 1:
                                flag1 = False
                                break
                        if not  flag1: break

                        for a in range(i, i+curlen+1):
                            if grid[a][j+curlen] != 1:
                                curlen += 1
                                flag2 = False
                                break
                        if not flag2: continue
                        for b in range(j, j + curlen + 1):
                            if grid[i+curlen][b] != 1:
                                curlen += 1
                                flag2 = False
                                break
                        if not  flag2: continue

                        curlen += 1
                        maxLen = curlen
        return maxLen*maxLen

