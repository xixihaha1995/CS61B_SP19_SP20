# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.tree = []
        self.inorder(root)
        minret = self.tree[-1]
        for i in range(1, len(self.tree)):
            minret = min(minret, self.tree[i] - self.tree[i - 1])
        return minret

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.tree.append(root.val)
        self.inorder(root.right)


