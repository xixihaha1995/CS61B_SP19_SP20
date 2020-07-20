class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.leng(root)
        return self.ans

    def leng(self, root):
        if not root: return 0
        l = self.leng(root.left) if root.left else -1
        r = self.leng(root.right) if root.right else -1
        pl = l + 1 if l >=0 and root.val == root.left.val else 0
        pr = r + 1 if r >= 0 and root.val == root.right.val else 0
        self.ans = max(self.ans, pl + pr)
        return max(pl, pr)