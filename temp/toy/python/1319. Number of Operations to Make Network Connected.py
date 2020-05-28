from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        self.parent = list(range(n))
        for conn in connections:
            self.parent[self.find(conn[0])] = self.parent[self.find(conn[1])]
        numroot = set()
        for i in range(n):
            numroot.add(self.find(i))
        return len(numroot) - 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]


if __name__ == '__main__':
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
    print(Solution().makeConnected(
        n, connections
    ))