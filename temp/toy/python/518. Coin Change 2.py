class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 : return 1
        if not coins: return 0
        dp = [0]*(amount+1)
        for coin in coins:
            for i in range(amount+1):
                if i < coin: continue
                dp[i] += dp[i-coin]
        return dp[-1]