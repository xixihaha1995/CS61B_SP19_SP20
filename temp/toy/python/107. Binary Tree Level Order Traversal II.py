# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
        nextLevelQueue = collections.deque()
        nextLevelQueue.append(root)
        result = []
        while nextLevelQueue:
            curLevel = []
            for i in range(len(nextLevelQueue)):
                curNode = nextLevelQueue.popleft()
                curLevel.append(curNode.val)
                if curNode.left:
                    nextLevelQueue.append(curNode.left)
                if curNode.right:
                    nextLevelQueue.append(curNode.right)
            result.append(curLevel)
        return result[::-1]
