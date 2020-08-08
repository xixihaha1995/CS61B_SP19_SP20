class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0] * len(A):
        temp = A[1] - A[0]
        for i in range(2,len(A)):
            curTemp = A[i] - A[i-1]
            if curTemp == temp:
                dp[i] += dp[i-1]
                temp = curTemp
        return sum(dp)

