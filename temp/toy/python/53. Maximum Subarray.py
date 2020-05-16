class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            num = max(res+num, num)
            res = max(res, res + num)
        return res