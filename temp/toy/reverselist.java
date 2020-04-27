/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val; try something
 * go on try something
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class reverselist {
    private class ListNode{
        int val;
        ListNode next;
        ListNode(int x){
            val =x;
        }
    }
    public ListNode reverseList(ListNode head) {
        ListNode curr = new ListNode();
        ListNode nextpoi = new ListNode();
        ListNode prev = new ListNode();
        curr = head;
//<<<<<<< HEAD
        prev = null;
//=======
        
//>>>>>>> origin/master
        while(curr != null) {
            nextpoi=curr.next;
            curr.next=prev;
            prev=curr;
            curr=nextpoi;
        }
        return prev;
    }
}
