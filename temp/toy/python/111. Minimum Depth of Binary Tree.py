# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return 1
        left_height = self.minDepth(root.left) if root.left else -sys.maxsize
        right_height = self.minDepth(root.right) if root.right else -sys.maxsize
        return min(left_height, right_height) + 1
