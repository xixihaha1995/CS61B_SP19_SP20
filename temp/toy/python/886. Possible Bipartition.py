class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        color = [0] * N
        for dis in dislikes:
            graph[dis[0]-1].append(dis[1]-1)
            graph[dis[1]-1].append(dis[0]-1)
        for i in range(N):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()
                for next in graph[cur]:
                    if color[next] != 0:
                        if color[next]== color[cur]: return False
                    else:
                        color[next] = -1 * color[cur]
                        bfs.append(next)
        return True