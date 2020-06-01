class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        d = float('inf')
        ans = 0
        for t in range(N-2):
            s, e = t + 1, N -1
            while s < e:

                sumthis = nums[t] + nums[s] + nums[e]

                if sumthis == target:
                    ans = target
                    return ans
                diff = abs(sumthis - target)
                if diff < d:
                    d = diff
                    ans = sumthis
                if sumthis > target: e -= 1
                else: s+= 1
        return ans