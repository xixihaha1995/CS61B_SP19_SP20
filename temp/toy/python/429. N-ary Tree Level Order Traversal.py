
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # queue utility and
        queue = [(root,0)]
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level+1))
        return res

if __name__ == '__main__':
    print(Solution().levelOrder(
        [1,None,3,2,4,None,5,6]
    ))
