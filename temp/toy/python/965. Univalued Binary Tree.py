# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# do something static and dynamic webpage
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = collections.deque()
        q.append(root)
        val = root.val
        while q:
            node = q.popleft()
            if not node:
                continue
            if node.val != val:
                return False
            q.append(node.left)
            q.append(node.right)
        return True

