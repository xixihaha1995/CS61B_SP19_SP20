class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        half = (m+n+1)/2
        left, right= 0, m
        while left < right:
            m1 = (left + right)//2
            m2 = half - m1
            if nums[m1] <nums[m2 -1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = half - left
        c1 = max(nums1[m1-1] if m1 >0 else float('-inf'), nums2[m2-1] if m2 > 0 else float('-inf'))
        if (m + n) % 2 == 1:
            return c1
        c2= min(nums1[m1] if m1< m else float('inf'), nums2[m2] if m2 <n else float('inf'))
        return (c1+c2)/2