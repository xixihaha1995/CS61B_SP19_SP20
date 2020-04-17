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

    public SLList (int x) {
        first = new IntNode(x, null);
    }
    public void addFirst(int i){
        first = new IntNode(i, first);
    }
    public void addLast(int i){
        IntNode p = first;
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
        return size(first);
    }

}