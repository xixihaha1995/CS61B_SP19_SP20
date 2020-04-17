public class SLList {

    private static class IntNode{
        public int item;
        public IntNode next;

        public IntNode(int i, IntNode n){
            item = i;
            next = n;
        }
    }
    private IntNode sentinel;
    private int count;

    public SLList () {
        sentinel = new IntNode(6, null);
        count=0;
    }
    public void addFirst(int i){
        sentinel.next = new IntNode(i, sentinel.next);
        count+=1;
    }
    public void addLast(int i){
        IntNode p = sentinel.next;
        count+=1;
        while(p.next != null) {
            p=p.next;
        }
        p.next= new IntNode(i, null);
    }
    public int getFirst(){
        return sentinel.next.item;
    }

    private static int size(IntNode p){
        if (p.next == null) {
            return 1;
        }
        return 1+size(p.next);
    }
    public int size(){
        return count;
    }

}