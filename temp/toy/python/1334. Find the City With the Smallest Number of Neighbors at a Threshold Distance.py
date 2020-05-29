class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for u, v, w in edges:
            d[u][v] = d[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[k][j])
        res = { sum(t <= distanceThreshold for t in d[i]) : i for i in range(n) }
        return res[min(res)]