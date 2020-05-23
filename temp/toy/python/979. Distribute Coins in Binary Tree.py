# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0
        self.balance(root, ans)
        return ans
    def balance(self, root, ans):
        if not root: return 0
        l = self.balance(root.left, ans)
        r =  self.balance(root.right, ans)
        ans += abs(l) + abs(r)
        return l + r + root.val - 1
