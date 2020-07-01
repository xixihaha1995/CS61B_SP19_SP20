class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        s += " "
        p += " "
        dp = [[False] * (n + 1) for _ in range( m+1 )]
        dp[0][0] = True
        for i in range(1,n+1):
            if p[i] == '*':
                dp[0][i] = dp[0][i-1]

        for j in range(1, n+1):
            for i in range(1, m+1):
                if p[j] != '*':
                    dp[i][j] == dp[i-1][j-1] and (s[i] == p[j] or p[j] == '?')
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]