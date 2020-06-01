class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        d = float('inf')
        ans = 0
        for t in range(N-2):
            s, e = t + 1, N -1
            while s < e:

                _sum = nums[t] + nums[s] + nums[e]

                if _sum == target:
                    ans = target
                    break
                diff = abs(_sum - target)
                if diff < d:
                    d = diff
                    ans = sum
                if _sum > target: e -= 1
                else: s += 1
        return ans