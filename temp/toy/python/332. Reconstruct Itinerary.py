from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edge = collections.defualtdict(list)
        for fro, to in tickets:
            edge[fro].append(to)
        to.sort(reverse = True)
        res = []
        self.dfs(edge, source, res)
        return res
    def dfs(self, edge, source, res):
        v = edge[source].pop()
        while edge[source]:
            self.dfs(edge, v, res)
        res.append(source)
