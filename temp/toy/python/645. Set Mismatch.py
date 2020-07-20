class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        dup = sum(nums) - sum(s)
        for i in range(nums[0], nums[-1])
            if i in s: continue
            else: dis = i
        return [dup, dis]