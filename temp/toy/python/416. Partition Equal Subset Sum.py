from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total / 2
        if target % 2 == 1: return False
        dp = [False] * (target + 1)
        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True
        for i in range(len(nums)):
            for j in range(target, nums[i]-1,-1):
                if dp[target]: return True
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]
        
print(Solution().canPartition(
    [1,5,5,11]
))

