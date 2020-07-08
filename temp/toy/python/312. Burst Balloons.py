from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        newnums = [1]* (len(nums)+2)
        for i in range(len(nums)):
            newnums[i+1] = nums[i]
        nums = newnums
        dp = [[0] * (n+2) for _ in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+1, n+2, 1):
                for k in range(i+1, j, 1):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[0][-1]

print(Solution().maxCoins(
    [3,1,5,8]
))