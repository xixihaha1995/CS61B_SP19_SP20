class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                if dp[i] >= 3: return True
        return False
