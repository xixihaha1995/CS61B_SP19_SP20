from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(i > 0 if dp[i-1] else 0 , i> 1 if dp[i-2]+nums[i] else 0)
        return dp[-1]

if __name__ == '__main__':
    print(Solution().rob(
        [2, 7, 9, 3, 1]
    ))
