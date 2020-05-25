from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        n = len(M)
        ans = 0
        for i in range (n):
            print(M)
            if M[i][i] == 1:
                ans += 1
                self.dfs(M,i,n)
        return ans
    def dfs(self, M, curr, n):
        for i in range(n):
            if M[curr][i] == 1:
                M[curr][i] = M[i][curr] = 0
                self.dfs(M, i, n)


if __name__ == '__main__':
    print(Solution().findCircleNum(
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    ))