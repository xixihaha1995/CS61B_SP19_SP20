class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]-1].append(dislike[1]-1)
            graph[dislike[1]-1].append(dislike[0]-1)
        color = [0] * N
        for i in range(N):
            if color[i] != 0 : continue

            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()

                for next in graph[cur]:
                    if color[next] != 0:
                        if color[next] == color[cur]: return False
                    else:
                        color[next] = -color[cur]
                        bfs.append(next)
        return True

