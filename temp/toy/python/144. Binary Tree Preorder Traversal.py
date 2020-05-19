class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        answer = []
        while root or stack:
            while root:
                stack.append(root)
                answer.append(root.val)
                root = root.left
            root = stack.pop().right
        return answer