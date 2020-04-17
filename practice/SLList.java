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
    public int getFirst(){
        return first.item;
    }

}