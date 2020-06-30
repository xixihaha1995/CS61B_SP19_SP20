class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('-inf')] * (target + 10)
        def helper(target):
            if dp[target] > 0: return dp[target]
            n = int(log(target, 2)) + 1
            if target == 2 **n - 1:
                dp[target] = n
            else:
                dp[target] = n + 1 + helper((2**n) - 1 - target)
                for m in range(n-1):
                    dp[target] = min (dp[target], n + m + 1 + (target - (2 **(n-1)) + (2**m)))
            return dp[target]
        return helper(target)