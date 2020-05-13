class Solution(object):
    def __init__(self):
        self.res = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(remainder, temp, count):
            if count == 0:
                self.res.append(temp)

            for i in remainder:
                if i in temp:
                    continue
                temp.append(i)
                remainder.remove(i)
                dfs(remainder, temp, count - 1)

       dfs(n,[], k)

if __name__ == '__main__':
    print(Solution().combine(4,2))