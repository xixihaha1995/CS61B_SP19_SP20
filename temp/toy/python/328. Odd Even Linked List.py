class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        odd, even, evenhead = head, head.next, even

        while not even and not even.next:
            odd.next = even.next
            odd = odd.next
            even.next= odd.next
            even = even.next

        odd.next = evenhead
        return head
