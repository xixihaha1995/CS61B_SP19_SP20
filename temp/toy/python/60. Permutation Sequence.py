import math

from xlwt.compat import xrange


class Solution(object):

    def __init__(self):
        self.res = []

    def getPermutation(self, n, k):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(n, temp, map):
            if n == 0:
                self.res.append(map[0])
                return
            for i in xrange(n):
                if i * math.factorial(n) < temp and (i + 1) * math.factorial(n) > temp:
                    res += map[i + 1]
                    map.remove(i + 1)
                    curdigit = i
                    break
            dfs(n - 1, temp - curdigit * curdigit, map)

        for i in xrange(n):
            map.append(i)
        dfs(n, k, map)
        return self.res


if __name__ == '__main__':
    print(Solution().getPermutation(4, 17))
