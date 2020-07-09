class Solution(object):
    def buildTree(self, preorder, inorder):
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])

        mid_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid_index], inorder[:mid_index])
        root.right  = self.buildTree(preorder[mid_index + 1 : ], inorder[mid_index + 1: ])

        return root