# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return answer
            root = stack.pop()
            answer.append(root.val)
            root = root.right

if __name__ == '__main__':
    print(Solution().inorderTraversal())
