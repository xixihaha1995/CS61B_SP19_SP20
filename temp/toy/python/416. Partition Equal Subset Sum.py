from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumall = sum(nums)
        if not sumall % 2: return False
        dp = [0] * (sumall + 1)
        dp[0] = 1
        for num in nums:
            for i in range(sumall,0,-1):
                if dp[i]: dp[i+num] = 1
            if dp[sumall/2]: return True
        return False

print(Solution().canPartition(
    [1,5,5,11]
))

