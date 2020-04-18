public class LinkedListDeque<genericType> {
    private class IntNode<IntNode,genericType,IntNode>{
        public IntNode prev;
        public genericType item;
        public IntNode next;

        public IntNode<IntNode p, genericType i, IntNode n>{
            prev = p;
            item = i;
            next = n;
        }
    }

    private IntNode<IntNode,genericType,IntNode> sentinel;
    private int size;

    public LinkedListDeque () {
        sentinel = new IntNode<>(null, 6, null);
        sentinel.prev = sentinel;
        sentinel.next = sentinel;
        size = 0;
    }
}

