class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return root
        queue = []
        queue.append(root)
        res= []
        while queue:
            temp = []
            for _ in range(len(queue)):
                node= queue.pop(0)
                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            level = len(temp)
            if level > 0:
                aver = sum(temp)/level
                res.append(aver)
        return  res