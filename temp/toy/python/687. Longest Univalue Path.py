class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        return self.leng(root)

    def leng(self, root):
        if not root: return 0
        cur = 1
        left = 0
        right = 0
        if root.right:
            if root.right.val == root.val:
                cur = cur + self.leng(root.right)
            else:
                right = self.leng(root.right)
        if root.left:
            if root.left.val == root.val:
                cur = cur + self.leng(root.left)
            else:
                left = self.leng(root.left)
        return max(cur, left, right)