class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower(nums, target)
        right = self.higher(nums, target)
        if left == right:
            return [-1, -1]
        else:
            return [left, right - 1]

    def lower(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = int((right + left) / 2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = int((right + left) / 2)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left