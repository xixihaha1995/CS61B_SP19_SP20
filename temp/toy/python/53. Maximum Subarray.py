from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            tmp = (nums[i] + nums[i-1]) if nums[i]>0 else nums[i-1]
            nums[i] = max(tmp, nums[i]) if nums[i] > 0 else nums[i]
        return nums[-1]

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))