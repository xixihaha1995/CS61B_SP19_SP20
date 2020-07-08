from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i-1]) if nums[i-1]>0 else nums[i]
            ans = max(ans, nums[i])
        return ans

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))