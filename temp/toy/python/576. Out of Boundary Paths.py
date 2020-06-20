class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[0]* n for _ in range(m)]
        dirc = [(1,0), (-1,0), (0,-1), (0,1)]
        for s in range(N):
            dp2 = [[0]* n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for intr, intc in dirc:
                        curr = r + intr
                        curc = c + intc
                        if curr < 0 or curr >= m or curc < 0 or curc >= n:
                            dp2[r][c] += 1
                        else:
                            dp2[r][c] = (dp2[r][c] + dp[curr][curc]) % (10**9 + 7)
            dp = dp2
            print(dp)
        return dp[i][j]

print(Solution().findPaths(
    2,2,2,0,0
))


