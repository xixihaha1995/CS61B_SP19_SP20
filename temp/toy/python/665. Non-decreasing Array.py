class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(1, len(nums)):
            if nums[i]>= nums[i-1]:
                continue
            if i-2 >= 0 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]
        return flag >= 1
