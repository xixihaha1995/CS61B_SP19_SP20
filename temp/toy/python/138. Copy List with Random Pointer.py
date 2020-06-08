
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = Node(0, None, None)
        temphead = head

        ans = cur
        while temphead:
            cur.val, cur.next, cur.random = temphead.val, temphead.next, temphead.random
            temphead = temphead.next
            cur = cur.next
        return ans

