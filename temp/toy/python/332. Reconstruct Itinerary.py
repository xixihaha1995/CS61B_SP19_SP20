from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edge = collections.defaultdict(list)
        for fro, to in tickets:
            edge[fro].append(to)
        for frm, to in edge.items():
            to.sort(reverse=True)
        res = []
        self.dfs(edge, "JFK", res)
        return res[::-1]

    def dfs(self, edge, source, res):

        while edge[source]:
            v = edge[source].pop()
            self.dfs(edge, v, res)
        res.append(source)
