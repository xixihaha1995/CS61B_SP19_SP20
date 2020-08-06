class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums2)
        store =dict()
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            store[nums2[i]] = res[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] =store[nums1[i]]
        return nums1