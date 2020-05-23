# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or head.next: return head
        root = ListNode(0)
        root.next = head
        while head.next:
            if head.val < head.next.val:
                head = head.next
            else:
                temp = head.next
                q = root
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return root.next
