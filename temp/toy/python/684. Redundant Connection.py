from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = [-1] * (len(edges)+1)
        for edge in edges:
            a = self.findRoot(edge[0], tree)
            b = self.findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge
    def findRoot(self, x, tree):
        if tree[x] == -1 : return x
        root = self.findRoot(tree[x], tree)
        tree[x] = root
        return root


if __name__ == '__main__':
    print(Solution().findRedundantConnection(
        [[1, 3], [2, 3], [1, 2]]
    ))

