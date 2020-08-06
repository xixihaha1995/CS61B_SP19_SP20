class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 : return 1
        if not coins: return 0
        m,n = amount+1, len(coins)
        dp = [[0]* n for _ in range(m)]
        dp[0] = [1] * n
        for i in range(1,m):
            if i % coins[0] == 0:
                dp[i][0] = 1
            else: dp[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1]
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i-coins[j]][j]
        return dp[-1][-1]