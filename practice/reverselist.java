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
        reverlist.val=head.val;
        
        ListNode pointer;
        ListNode repointer;
        pointer = head;
        repointer=reverlist;
        while(head != null) {
             while(pointer.next != null) {
                pointer=pointer.next;
            }
            repointer.val=pointer.val;
            repointer=repointer.next;
            pointer=pointer.next;
        }
        return reverlist;
           
        
    }
}
