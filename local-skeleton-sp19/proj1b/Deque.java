public interface Deque<genericType> {
//    public int size;
    public void addFirst(genericType i);
    public void addLast(genericType i);

    public int size();
    default boolean isEmpty(){
        if (size() == 0) {
            return true;
        }else {
            return false;
        }
    }
    public void printDeque();
    public genericType removeFirst();
    public genericType removeLast();
    public genericType get(int index);



}
