import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        visited = set()
        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0/value
        cur = 0
        for (x, y) in queries:
            if x in table and y in table:
                cur = self.dfs(table, x, y,visited)
            else:
                cur = -1.0
            ans.append(cur)
        return ans
    def dfs(self, table, x, y, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for next in table[x]:
            if next in visited: continue
            d = self.dfs(table,next, y, visited)
            if d > 0:
                return d * table[x][next]
        return -1.0

if __name__ == '__main__':
    print(Solution().calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ))