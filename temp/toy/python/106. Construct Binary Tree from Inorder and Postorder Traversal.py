class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder and postorder):
            return None
        self.post_idx = len(postorder) - 1
        d = {val: idx for idx, val in enumerate(inorder)}

        def dfs(left,right):
            if left > right:
                return None
            val = postorder[self.post_idx]
            root = TreeNode(val)
            self.post_idx -= 1
            index = d[val]
            root.right = dfs(index+1, right)
            root.left = dfs(left, index - 1)

        return dfs(0, len(postorder) -1 )