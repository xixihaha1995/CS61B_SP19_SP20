import java.util.Iterator;
import java.util.Set;



public class BSTMap<K extends Comparable<K>,V> implements Map61B<K, V>{
    private class BST{
        public BST left;
        public BST right;
        public K key;
        private V value;

        public  BST(K i, V val,BST l, BST r){
            left = l;
            right = r;
            key = i;
            value = val;
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
        return numbers;
    }

    @Override
    public boolean containsKey(K key) {
        return false;
    }

    @Override
    public void put(K key, V value) {

    }
    public void printInOrder(){

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


}
