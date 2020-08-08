class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [root]
        res = 0
        while queue:
            node = queue.pop()
            if node:
                if node.left and (not node.left.left and not node.left.right):
                    res += node.left.val
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return res