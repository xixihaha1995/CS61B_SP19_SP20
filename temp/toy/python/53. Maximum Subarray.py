from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [0] * (len(nums))
        res[0] = nums[0]
        for i in range(1,len(nums)):
            res[i] = max(nums[i], res[i-1] + nums[i])
        return max(res)

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))