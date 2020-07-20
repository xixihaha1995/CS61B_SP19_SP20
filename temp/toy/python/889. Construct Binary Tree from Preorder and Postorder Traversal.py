class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None

        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        leftRoot = pre[1]
        leftCount = post.index(leftRoot)

        root.left = self.constructFromPrePost(pre[1: 1 + 1 + leftCount], post[: leftCount + 1])
        root.right = self.constructFromPrePost(pre[2 + leftCount:], post[leftCount + 1: -1])
        return root