class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        left = 0
        for _ in range(len(nums)):
            if nums[left] != nums_sort[left]:
                break
            left += 1
        if left == len(nums):
            return 0

        right = len(nums) - 1
        for _ in range(len(nums) - 1, -1, -1):
            if nums[right] != nums_sort[right]:
                break
            right -= 1
        return right - left + 1

