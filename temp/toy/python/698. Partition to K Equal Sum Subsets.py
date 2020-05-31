from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k: return False
        _sum = sum(nums)
        div, mod = divmod(_sum, k)
        if _sum % k: return  False
        nums.sort(reverse = True)
        target = [div] * k
        return self.dfs(nums, k, 0, target)
    def dfs(self, nums, k, index, target):
        if index == len(nums): return True
        num = nums[index]
        for i in range(k):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, k, index + 1, target): return True
                target[i] += num
        return False

if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]; k = 4
    print(Solution().canPartitionKSubsets(
        nums,k
    ))

