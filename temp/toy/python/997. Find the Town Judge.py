from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        stat = [0]* N
        for trust_pair in trust:
            stat[trust_pair[0] -1] -= 1
            stat[trust_pair[1] -1] += 1
        for i in range(N):
            if stat[i] == (N-1):
                return i + 1
        return -1

if __name__ == '__main__':
    print(Solution().findJudge(
       3, [[1, 3], [2, 3], [3, 1]]
    ))
