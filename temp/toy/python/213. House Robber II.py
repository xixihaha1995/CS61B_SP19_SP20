from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.robrange(nums[0:-2]), self.robrange(nums[1:-1]))

    def robrange(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = max(dp[i - 1] if i > 0 else nums[i], dp[i - 2] + nums[i] if i > 1 else nums[i])
        return dp[-1]

if __name__ == '__main__':
    print(Solution().rob(
        [1,2,3,1]
    ))