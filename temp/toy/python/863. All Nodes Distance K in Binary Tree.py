# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        conn = collections.defaultdict(list)
        def connect(parent, children):
            if parent and children: conn[parent].append(children)
            if children.left: connect(children, children.left)
            if children.right: connect(children, children.right)
        connect(None, root)


if __name__ == '__main__':
    root = TreeNode()
    print(Solution().distanceK(

    ))
