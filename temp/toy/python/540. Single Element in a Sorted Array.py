class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if mid % 2 != 0 and mid + 1 < len(nums):
                if nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:left = mid + 1
            elif mid % 2 == 0 and mid + 1 < len(nums):
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:right = mid - 1
            else:
                return nums[mid]
        return nums[left]

