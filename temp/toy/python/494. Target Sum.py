class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        allPos = sum(nums)
        if (allPos + S) % 2 != 0 or S > allPos: return 0
        cap = int((allPos + S ) /2)
        dp = [0] * (cap + 1)
        dp[0] = 1
        for ele in nums:
            for i in range(cap, ele-1, -1):
                dp[i] += dp[i-ele]
        return dp[cap]