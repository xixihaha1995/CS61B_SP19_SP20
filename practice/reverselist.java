/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode reverlist = new ListNode();
        ListNode temp = new ListNode();
        reverlist.val=head.val;
        while(head != null) {
            head=head.next;
            temp.val=head.val;
            temp.next=reverlist;
            reverlist=temp;
        }
        return reverlist;
    }
}
