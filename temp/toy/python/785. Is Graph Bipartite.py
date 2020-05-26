import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        for i in range(len(graph)):
            if visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft()
                    for next in graph[v]:
                        if visited[next] != 0:
                            if visited[v] == visited[next]:
                                return False
                        else:
                            visited[next] = 3 - visited[v]
                            q.append(next)
        return True

if __name__ == '__main__':
    print(Solution().isBipartite(
        [[1, 3], [0, 2], [1, 3], [0, 2]]
    ))