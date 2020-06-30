import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)

        que = collections.deque()
        for i in range(len(indegrees)):
            if not indegrees[i]: que.append(i)
        ans = []
        while que:
            pre = que.popleft()
            ans.append(pre)
            numCourses -= 1
            for cur in adj[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: que.append(cur)
        return ans