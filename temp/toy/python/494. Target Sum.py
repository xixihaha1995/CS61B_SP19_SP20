class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        allPos = sum(nums)
        if (allPos + S) % 2 != 0 or S > allPos: return 0
        cap = (allPos + S ) /2
        dp = [0] * (cap + 1)
        dp[0] = 1
        for num in nums:
            for i in range(cap, -1, -1):
                dp[i] += dp[i-nums]
        return dp[cap]
