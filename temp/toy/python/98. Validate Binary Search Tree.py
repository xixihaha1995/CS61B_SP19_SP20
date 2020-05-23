# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if root.left:
            if root.left.val >= root.val:
                return False
            self.isValidBST(root.left)
        if root.right:
            if root.right.val <= root.val:
                return False
            self.isValidBST(root.right)
