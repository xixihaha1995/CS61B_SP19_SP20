class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums)-1):
            p *= nums[i]
            res.append(p)
        for i in range(len(nums), -1, -1):
            q *= nums[i]
            res[i] *= q
        return res
