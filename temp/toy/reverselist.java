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
            next = null;
        }
    }
    public ListNode curr;
    public ListNode nextpoi;
    public ListNode prev;
    public ListNode reverseList(ListNode head) {
        curr = new ListNode(5);
        nextpoi = new ListNode(5);
        prev = new ListNode(5);
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
