# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        res =  []
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            node = queue.popleft()
            for i in range(len(queue)):
                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
        return res
