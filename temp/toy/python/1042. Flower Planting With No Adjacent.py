class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        graph = [[] for _ in range(N)]
        for path in paths:
            graph[path[0]-1].append(path[1]-1)
            graph[path[1]-1].append(path[0]-1)
        for i in range(N):
            neighbour_colors = []
            for neighbour in graph[i]:
                if res[neighbour] != 0:
                    neighbour_colors.append(res[neighbour])
            for color in range(1,5):
                if color in neighbour_colors:
                    continue
                res[i] = color
                break
        return res
