class Solution:
    def minSteps(self, n: int) -> int:
        d = 2
        ans = 0
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
print(Solution().minSteps(30))
