class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        a = set()
        find = 0
        def dfs(root):
            nonlocal find
            if root.left: dfs(root.left)
            if k - root.val in a : find = 1
            a.add(root.val)
            if root.right: dfs(root.right)
        dfs(root)
        return True if find else False