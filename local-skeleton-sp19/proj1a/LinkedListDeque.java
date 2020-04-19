public class LinkedListDeque<genericType> {
    private class genericNode{
        public genericNode prev;
        public genericType item;
        public genericNode next;

        public genericNode(genericNode p, genericType i, genericNode n){
            prev = p;
            item = i;
            next = n;
        }
        
    }

    private genericNode sentinel;
    private int size;

    public LinkedListDeque () {
        sentinel = new genericNode(null, null, null);
        sentinel.prev = sentinel;
        sentinel.next = sentinel;
        size = 0;
    }
}

