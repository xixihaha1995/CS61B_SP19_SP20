class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        totalLen = 0
        cur = root
        while cur:
            totalLen += 1
            cur = cur.next
        length = totalLen // k
        mod = totalLen % 3
        res = []
        cur = root
        for i in range(k):
            res.append(cur)
            size = length + (1 if m > 0 else 0)
            if cur:
                for j in range(size):
                    cur = cur.next
                tmp = cur.next
                cur.next = None
                cur = tmp
        return res

