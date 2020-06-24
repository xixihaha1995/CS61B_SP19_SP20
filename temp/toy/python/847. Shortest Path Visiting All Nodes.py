from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if graph == [[]]: return 0
        queue = [(i, 1<<i) for i in range(len(graph))]
        visited = {i:[1<<i] for i in range(len(graph))}

        path = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                i, state = queue.pop(0)

                if state == (1<<len(graph) )- 1:
                    print(1<<len(graph) - 1)
                    return path
                for nei in graph[i]:
                    if (state | 1<< nei) not in visited[nei]:
                        print(state |1 <<  nei)
                        visited[nei].append(state | 1<<nei)
                        queue.append(((nei, state |1<<nei)))
            path = path + 1

print(Solution().shortestPathLength(
    [[1,2,3],[0],[0],[0]]
))