class LFUCache {
    Map<Integer, Node> cache;
    DoublyLinkedList firstLinkedList;
    DoublyLinkedList lastLinkedList;
    int size;
    int capacity;


    public LFUCache(int capacity) {
        cache = new HashMap<>(capacity);
        firstLinkedList = new DoublyLinkedList();
        lastLinkedList = new DoublyLinkedList();
        firstLinkedList.post = lastLinkedList;
        lastLinkedList.pre = firstLinkedList;
        this.capacity = capacity;
    }

    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) {
            return -1;
        }
        freqInc(node);
        return node.value;
    }

    public void put(int key, int value) {
        if (this.capacity  == 0) {
            return;
        }
        Node node = cache.get(key);
        if(node != null) {
            node.value = value;
            freqInc(node);
        }else{
            if (size == capacity) {
                cache.remove(lastLinkedList.pre.tail.pre.key);
                lastLinkedList.removeNode(lastLinkedList.pre.tail.pre);
                size--;
            }
            if (lastLinkedList.pre.head.post == lastLinkedList.pre.tail) {
                removeDoublyLinkedList(lastLinkedList.pre);
            }
        }
        Node newNode = new Node(key, value);
        cache.put(key,newNode);
        if (lastLinkedList.pre.freq != 1) {
            DoublyLinkedList newDoublyLinkedList = new DoublyLinkedList(1);
            addDoublyLinkedList(newDoublyLinkedList, lastLinkedList.pre);
            newDoublyLinkedList.addNode(newNode);
        } else {
            lastLinkedList.pre.addNode(newNode);
        }
        size++;
    }

    void freqInc(Node node) {
        DoublyLinkedList linkedList = node.doublyLinkedList;
        DoublyLinkedList preLinkedList = linkedList.pre;
        linkedList.removeNode(node);
        if (linkedList.head.post == linkedList.tail) {
            removeDoublyLinkedList(linkedList);
        }
        node.freq++;
        if(preLinkedList.freq != node.freq) {
            DoublyLinkedList newDoublyLinkedList = new DoublyLinkedList(node.freq);
            addDoublyLinkedList(newDoublyLinkedList, preLinkedList);
            newDoublyLinkedList.addNode(node);
        } else{
            preLinkedList.addNode(node);
        }
    }
    void addDoublyLinkedList(DoublyLinkedList newDoublyLinkedList, DoublyLinkedList preLinkedList) {
        newDoublyLinkedList.post = preLinkedList.post;
        newDoublyLinkedList.post.pre = newDoublyLinkedList;
        newDoublyLinkedList.pre = preLinkedList;
        preLinkedList.post = newDoublyLinkedList;
    }

    void removeDoublyLinkedList(DoublyLinkedList doublyLinkedList) {
        doublyLinkedList.pre.post = doublyLinkedList.post;
        doublyLinkedList.post.pre = doublyLinkedList.pre;
    }
}

class Node{
    int key;
    int value;
    int freq  = 1;

    Node pre;
    Node post;
    DoublyLinkedList doublyLinkedList;

    public Node(int key, int value){
        this.key = key;
        this.value = value;
    }
}

class DoublyLinkedList{
    DoublyLinkedList pre;
    DoublyLinkedList post;
    Node head;
    Node tail;

    public DoublyLinkedList() {
        head = new Node();
        tail = new Node();
        head.post = tail;
        tail.pre = head;
    }
    public DoublyLinkedList(int freq) {
        head = new Node();
        tail = new Node();
        head.post = tail;
        tail.pre = head;
        this.freq = freq;
    }

    void removeNode(Node node) {
        node.pre.post = node.post;
        node.post.pre = node.pre;
    }

    void addNode(Node node) {
        node.post = head.post;
        head.post.pre = node;
        head.post = pre;
        node.pre = head;
        node.doublyLinkedList = this;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */