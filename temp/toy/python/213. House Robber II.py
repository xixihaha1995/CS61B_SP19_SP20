class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.robRange(nums[0:-2]), self.robRange(nums[1:-1])

    def robRange(self, nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums)
            n = len(nums)
            dp = [0] * n
            for i in range(1,n):
                dp[i] = max(dp[i-1] if i>0 else nums[i], dp[i-2] if i>1 else nums[i])
            return dp[-1]