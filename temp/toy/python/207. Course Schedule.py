import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for _ in range (numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)

        que = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                que.append(i)

        while que:
            pre = que.popleft()
            numCourses -= 1
            for cur in adj[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: que.append(cur)
        return not numCourses


