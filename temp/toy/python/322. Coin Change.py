from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float 'inf'] * (amount+1)
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[-1] == float 'inf' else dp[-1]

if __name__ == '__main__':
    print(Solution().coinChange(
        [186, 419, 83, 408], 6249
    ))
