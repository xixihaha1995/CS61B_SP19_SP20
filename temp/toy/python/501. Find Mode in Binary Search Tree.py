class Solution:
    def __init__(self):
        self.cur = None
        self.curtimes = 0
        self.lasttimes = 0
        self.modes = []
    def findMode(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return self.modes

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if self.lasttimes == 0:
            self.lasttimes = 1
        if root.val != self.cur:
            self.curtimes = 0
        self.cur = root.val
        self.curtimes += 1
        if self.curtimes == self.lasttimes:
            self.modes.append(self.cur)
        if self.curtimes > self.lasttimes:
            self.lasttimes = self.curtimes
            self.modes.clear()
            self.modes.append(self.cur)
        self.inorder(root.right)
