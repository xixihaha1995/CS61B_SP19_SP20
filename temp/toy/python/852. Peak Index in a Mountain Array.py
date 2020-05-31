class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0,  len(A)
        while left < right:
            mid = int((left + right)/2)
            if A[mid]>A[mid+1]:
                right = mid
            else:left = mid + 1