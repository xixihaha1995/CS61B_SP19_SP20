class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        dp = [0] * len(A)
        temp = A[1] - A[0]
        for i in range(2,len(A)):
            curTemp = A[i] - A[i-1]
            if curTemp == temp:
                dp[i] = 1+ dp[i-1]
            else:
                temp = curTemp
        return sum(dp)

