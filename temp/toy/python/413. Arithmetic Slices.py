class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        left, right = 0,0
        valid = 0
        while right < len(A):
            right += 1
            while right - left >= 2:

