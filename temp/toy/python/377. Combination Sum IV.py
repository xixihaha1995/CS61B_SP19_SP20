from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memor = [-1]*(target+1)
        memor[0] = 1
        return self.helper(nums, target,memor)
    def helper(self, nums, target,memor):
        if target < 0: return 0
        if memor[target] != -1: return memor[target]
        ans = 0
        for num in nums:
            if num <= target:
                ans += self.helper(nums, target-num,memor)
                memor[target] = ans
        return ans

print(Solution().combinationSum4(
    [1,2,3], 4
))