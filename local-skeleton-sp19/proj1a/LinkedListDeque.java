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
    public void addFirst(genericType i){
        sentinel.next.prev = new genericNode(sentinel, i, sentinel.next);
        sentinel.next = sentinel.next.prev;
        size += 1;
    }
    public void addLast(genericType i){
        sentinel.prev.next = new genericNode(sentinel.prev, i, sentinel);
        sentinel.prev = sentinel.prev.next;
        size += 1;
    }
    public boolean isEmpty(){
        if (size == 0){
            return true;
        }else{
            return false;
        }
    }
    public int size(){
        return size;
    }
    public void printDeque(){
        genericNode p = sentinel.next;
        while(p != sentinel){
            System.out.print(p.item);
            p = p.next;
        }
    }
    public genericType removeFirst(){
        sentinel.next = sentinel.next.next;
        sentinel.next.prev = sentinel;
        size -= 1;
        if (size>0){
            return sentinel.next.item;
        }else{
            return null;
        }
    }
    public genericType removeLast(){
        sentinel.prev = sentinel.prev.prev;
        sentinel.prev.next = sentinel;
        size -=1;
        if (size>0){
            return sentinel.prev.item;
        }else{
            return null;
        }
    }
    public genericType get(int index){
        genericNode p = sentinel.next;
        for(int i = 0; i< index; i++){
            p = p.next;
        }
        return p.item;
    }
    public LinkedListDeque(LinkedListDeque other){
        sentinel = other.sentinel;
        size = other.size();
        for(int i = 0; i< size; i++){
            addLast((genericType) other.get(i));
        }

    }
    public genericType getRecursive(int index){
        genericNode p =sentinel.next;
        return getRecursive(p, index);

    }
    private genericType getRecursive(genericNode poin, int index){
        if(index==0){
            return poin.item;
        }
        return getRecursive(poin.next,index-1);

    }
}

