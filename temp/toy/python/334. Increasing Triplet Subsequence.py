class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return dp[-1]
