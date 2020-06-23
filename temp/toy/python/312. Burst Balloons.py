from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
            if left == right - 1: return 0
            return max(nums[left]*nums[i]*nums[right] + dp(left,i) + dp(i, right) for i in range(left+1, right))

        return dp(0, len(nums) - 1)

print(Solution().maxCoins(
    [3,1,5,8]
))