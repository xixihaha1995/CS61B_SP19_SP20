class Solution:
    def dfs(self, graph, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            if graph[i][j] == 1:
                if colors[j] == color: return False
                if colors[j] == 0  and not self.dfs(graph, colors, j, -1 * color, N):
                    return False
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[0]*N for _ in range(N)]
        colors = [0]*N
        for dis in dislikes:
            graph[dis[0]-1][dis[1]-1] = 1
            graph[dis[1]-1][dis[0] - 1] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1, N):
                return False
        return True