from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for num in nums:
            tmp = dp[:]
            for s in tmp:
                dp[(s + num) % 3] = max(dp[(s + num) % 3], s + num)
        return dp[0]

print(Solution().maxSumDivThree(
    [3,6,5,1,8]
))