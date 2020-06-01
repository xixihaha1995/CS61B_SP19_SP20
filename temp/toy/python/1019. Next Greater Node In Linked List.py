class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        res = [0] * len(nums)
        stack=[]
        for i,n in nums:
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        return res