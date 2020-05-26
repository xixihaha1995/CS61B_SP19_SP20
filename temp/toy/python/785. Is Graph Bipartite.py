from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        for i in range(len(graph)):
            visited[i] =

if __name__ == '__main__':
    print(Solution().isBipartite(
        [[1, 3], [0, 2], [1, 3], [0, 2]]
    ))