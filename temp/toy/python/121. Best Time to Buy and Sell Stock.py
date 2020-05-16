from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        dp = [0] * len(prices)
        for i in range (1, len(prices)):
            minP = min(prices[i], minP)
            dp[i] = max(dp[i-1], prices[i]-minP)
        return dp[-1]

if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))