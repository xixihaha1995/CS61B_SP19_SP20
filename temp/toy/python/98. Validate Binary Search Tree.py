# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.valid(root, -float('inf'), float('inf'))
    def valid(self, root, minnum, maxnum):
        if not root: return True
        if root.val <= minnum or root.val >= maxnum:
            return False
        else
            return self.valid(root.left,minnum, root.val) and self.valid(root.right, root.val, maxnum)