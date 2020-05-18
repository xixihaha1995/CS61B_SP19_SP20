from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max( dp[i-1] if i>0 else nums[i] , dp[i-2]+nums[i] if i > 1 else nums[i])
        return dp[-1]

if __name__ == '__main__':
    print(Solution().rob(
        [2,1]
    ))
