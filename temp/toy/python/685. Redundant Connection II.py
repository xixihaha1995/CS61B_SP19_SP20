class UnionFind(object):
    def __init__(self,n):
        self.pre = list(range(n))
    def find(self,x):
        if x != self.pre[x]:
            self.pre[x] = self.pre(self.pre[x])
        return self.pre[x]
    def union(self,x, y):
        root2 = self.find(y)
        root1 = self.find(x)

        if root1 != root2:
            self.pre[root2] = root1
            return False
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)

        last = []
        parent = []
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


