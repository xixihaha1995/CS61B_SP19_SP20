class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
            def union(self, x, y):
                rootx = self.find(x)
                rooty = self.find(y)

                if rootx != rooty:
                    self.parent[rootx] = rooty
            def find(self, x):
                while x != self.parent[x]:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            max_val = max(A)
            unionfind = UnionFind(max_val + 1)
            //先把所有数的factor和i 连接
            for num in A:
                upbound = int(sqrt(num))
                for i in range(2, upbound + 1):
                    if num % i == 0:
                        unionfind.union(num, i)
                        unionfind.union(num, num//i)

            cnt = [0] * (max_val + 1)
            res = 0
            for num in A:
                root = unionfind.find(num)
                cnt[root] += 1
                res = max(res, cnt[root])
            return res

