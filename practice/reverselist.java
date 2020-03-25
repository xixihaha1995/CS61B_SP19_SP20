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
        ListNode pointer = new ListNode();
        ListNode old = new ListNode();
        pointer = head;
        old=pointer;
        reverlist=old;
        reverlist.next=null;
        while(pointer.next != null) {
            pointer=pointer.next;
            reverlist=old;
            reverlist.next=old;
            old=old.next;
        }
        return reverlist;
    }
}
