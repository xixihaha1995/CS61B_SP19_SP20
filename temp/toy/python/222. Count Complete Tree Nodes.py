class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def countLevel(root):
            level = 0
            while root != None:
                level += 1
                root = root.left
            return level

        left = countLevel(root.left)
        right = countLevel(root.right)

        if left == right:
            return self.countNodes(root.right) + (1<<left)
        else:
            return self.countNodes(root.left) + (1<<right)
