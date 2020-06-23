from typing import List

from xlwt.compat import xrange


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        memo = [[[None]* N for _ in xrange(N)]for _ in xrange(N)]

        def dp(r1, c1, c2):
            r2 = r1 + c1 -c2
            if (N == r1 or N ==r2 or N == c1 or grid[r1][c1] == -1
                    or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif memo[r1][c1][r2] is not None:
                return memo[r1][c1][r2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1, c1+1, c2+1), dp(r1+1, c1, c2+1),
                           dp(r1, c1+1,c2), dp(r1+1, c1, c2))
            memo[r1][c1][r2] = ans
            return ans
        return max(0, dp(0,0,0))

print(Solution().cherryPickup(
    [[0, 1, -1],
     [1, 0, -1],
     [1, 1,  1]]
))