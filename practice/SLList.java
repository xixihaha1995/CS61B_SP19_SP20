public class SLList {

    private static class IntNode{
        public int item;
        public IntNode next;

        public IntNode(int i, IntNode n){
            item = i;
            next = n;
        }
    }
    private IntNode first;
    private int count;

    public SLList (int x) {
        first = new IntNode(x, null);
        count=1;
    }
    public void addFirst(int i){
        first = new IntNode(i, first);
        count+=1;
    }
    public void addLast(int i){
        IntNode p = first;
        count+=1;
        while(p.next != null) {
            p=p.next;
        }
        p.next= new IntNode(i, null);
    }
    public int getFirst(){
        return first.item;
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