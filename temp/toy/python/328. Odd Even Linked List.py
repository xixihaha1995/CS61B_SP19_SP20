class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        odd, even = head, head.next
        evenhead = even

        while  even and  even.next:
            odd.next = even.next
            odd = odd.next
            even.next= odd.next
            even = even.next

        odd.next = evenhead
        return head
