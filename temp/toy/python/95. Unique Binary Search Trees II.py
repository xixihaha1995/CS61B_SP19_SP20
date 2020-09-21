from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.helper(1,n)

    def helper(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            leftNodes = self.helper(left, i-1)
            rightNodes = self.helper(i+1, right)

            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        return res

print(Solution().generateTrees(3))