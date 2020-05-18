from _testcapi import INT_MIN
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        rest = 0
        sold = 0
        hold = -prices[0]
        for i in range(len(prices)):
            prev_hold = sold
            sold = hold + prices[i]
            hold = max(hold, rest-prices[i])
            rest = max(rest, prev_hold)
        return max(rest, sold)

if __name__ == '__main__':
    print(Solution().maxProfit(
        [1, 2, 3, 0, 2]
    ))
