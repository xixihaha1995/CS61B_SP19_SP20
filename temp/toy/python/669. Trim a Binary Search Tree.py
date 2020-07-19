class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root: return root
        if root.val < L: return self.trimBST(root.right, L, R)
        if root.val > R: return self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        root.left = self.trimBST(root.left, L, R)
        return root

