class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [0] * n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            res[i%n] = -1 if not stack else stack[-1]
            stack.append(i%n)
        return res
