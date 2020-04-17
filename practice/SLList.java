public class SLList {
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