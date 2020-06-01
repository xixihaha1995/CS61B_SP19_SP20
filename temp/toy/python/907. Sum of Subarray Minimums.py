from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        kMod = 10**9 + 7
        n = len(A)
        s, left, right = [], [1]*n, [1]*n
        for i in range(n):
            while s and s[-1][0] > A[i]:
                left[i] += s.pop()[1]
            s.append((A[i],left[i]))
        s = []
        for i in range(n-1, -1, -1):
            while s and s[-1][0] >= A[i]:
                right[i] += s.pop()[1]
            s.append((A[i], right[i]))
        ans = sum(a * l * r for a, l, r in zip(A, left, right)) % kMod
        return ans


if __name__ == '__main__':
    print(Solution().sumSubarrayMins(
        [3, 1, 2, 4]
    ))