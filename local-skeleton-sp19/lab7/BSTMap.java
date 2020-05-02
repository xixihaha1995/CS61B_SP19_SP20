import java.util.Iterator;
//import java.util.Queue;
import java.util.Set;



public class BSTMap<K extends Comparable<K>,V> implements Map61B<K, V>{
    private class BST{
        private BST left, right;
        private K key;
        private V value;
        private int size;

        public  BST(K i, V val,int size){
            key = i;
            value = val;
            this.size = size;
        }
    }

    private BST biSeTr;
    public int numbers;

    public BSTMap(){
    }


    @Override
    public void clear() {
        numbers = 0;
        biSeTr = null;

    }
    @Override
    public V get(K key) {
        return get(biSeTr,key);
    }
    private V get(BST x, K key){
        if (key == null) throw new IllegalArgumentException("calls get() with a null key");
        if (x == null) return null;
        int cmp = key.compareTo(x.key);
        if      (cmp < 0) return get(x.left, key);
        else if (cmp > 0) return get(x.right, key);
        else              return x.value;

    }
    @Override
    public int size() {
        return size(biSeTr);
    }
    private int size(BST bst){
        if (bst == null) return 0;
        else return bst.size;
    }

    @Override
    public boolean containsKey(K key) {
        if ( key == null) {
            throw new IllegalArgumentException("argument to contains() is null");
        }
        return get(key) != null;
    }

    @Override
    public void put(K key, V value) {
        if(key == null) throw new IllegalArgumentException("calls put() with a null key");
        biSeTr = put(biSeTr,key, value);

    }
    private BST put(BST x, K key, V val){
        if (x == null) return new BST(key, val, 1);
        int cmp = key.compareTo(x.key);
        //TODO understand how put() works
        if ( cmp < 0 )
            x.left = put(x.left, key, val);
         else if ( cmp > 0 )
            x.right = put(x.right, key, val);
         else x.value = val;
        x.size = 1 + size(x.left) + size(x.right);
        return x;

    }
    public boolean isEmpty() {
        return size() == 0;
    }
    public Iterable<K> keys(){
        if (isEmpty()) return new Queue<K>();
        return keys(min(), max());
    }
    public K min(){
        return min(biSeTr).key;
    }
    private BST min(BST x){
        if (x.left == null) return x;
        else return min(x.left);
    }
    public K max(){
        return max(biSeTr).key;
    }
    private BST max(BST x){
        if (x.right == null) return x;
        else return min(x.right);
    }

    public Iterable<K> keys(K lo, K hi) {
        Queue<K> queue = new Queue<K>();
        keys(biSeTr,queue, lo, hi);
        return queue;
    }
    private void keys(BST x, Queue<K> queue, K lo, K hi) {
        if (x == null) return;
        int cmplo = lo.compareTo(x.key);
        int cmphi = hi.compareTo(x.key);
        if (cmplo < 0) keys(x.left, queue, lo, hi);
        if (cmplo <= 0 && cmphi >= 0) queue.enqueue(x.key);
        if (cmphi > 0) keys(x.right, queue, lo, hi);

    }


    public void printInOrder(){
        for (K s: keys()){
            StdOut.println(s + " " + get(s));
        }

    }
    @Override
    public V remove(K key) {
        throw new UnsupportedOperationException();
    }

    @Override
    public V remove(K key, V value) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Set<K> keySet() {
        throw new UnsupportedOperationException();
    }

    @Override
    public Iterator<K> iterator() {
        throw new UnsupportedOperationException();
    }

/*    @Override
    public Set<K> keySet() {
        return null;
    }

    @Override
    public V remove(K key) {
        return null;
    }

    @Override
    public V remove(K key, V value) {
        return null;
    }*/

/*    @Override
    public int compareTo(K k) extends Comparable<K> {
        return 0;
    }*/
public static void main(String[] args) {
    BSTMap<String, Integer> b = new BSTMap<String, Integer>();
    BSTMap<String, Integer> st = new BSTMap<String, Integer>();
    st.get("starChild");
    st.put("starChild", 5);
    st.put("bob", 5);
    st.put("car", 5);
    st.put("put", 5);
    st.put("zoo", 5);
    st.put("water", 5);
    st.put("toy", 5);
    st.printInOrder();
}


}
