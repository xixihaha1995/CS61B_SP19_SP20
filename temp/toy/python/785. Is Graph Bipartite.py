from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = [0] * len(graph)
        for i in range(len(graph)):
            if not self.coloring(graph, i, 0,colored): return False
        return True
    def coloring(self, graph, node, color,colored):
        if node in colored:
            return colored[node] == 1
        colored[node] = 1
        for next in graph[node]:
            if not self.coloring(graph, next, 1, colored): return False
            colored[next] = -1
        return True


if __name__ == '__main__':
    print(Solution().isBipartite(
        [[1, 3], [0, 2], [1, 3], [0, 2]]
    ))