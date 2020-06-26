# coding:utf-8

class UnionFind(object):

    def __init__(self, n):
        self.pre = range(n)

    def find(self, x):
        if x != self.pre[x]:
            self.pre[x] = self.find(self.pre[x])
        return self.pre[x]

    def union(self, x1, x2):
        root1 = self.find(x1)
        root2 = self.find(x2)
        if root1 != root2:
            self.pre[root2] = root1
            return False

        return True

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        uf = UnionFind(n + 1)

        last = []
        parent = {}
        candidates = []
        for st, ed in edges:
            if ed in parent:
                candidates.append([parent[ed], ed])
                candidates.append([st, ed])
            else:
                parent[ed] = st
                if uf.union(st, ed):
                    last = [st, ed]

        if not candidates:
            return last

        return candidates[0] if last else candidates[1]

