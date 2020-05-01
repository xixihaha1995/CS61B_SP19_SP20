import java.util.Iterator;
import java.util.Set;

public class BSTMap<K,V> implements Map61B<K, V>, Comparable<K> {
    private static class BST{
        public BST left;
        public BST right;
        public K item;

        public  BST(K i, BST l, BST r){
            left = l;
            right = r;
            item = i;
        }
    }
    private BST biSeTr;
    public int numbers;


    @Override
    public void clear() {

    }

    @Override
    public boolean containsKey(K key) {
        return false;
    }

    @Override
    public V get(K key) {
        return null;
    }

    @Override
    public int size() {
        return 0;
    }

    @Override
    public void put(K key, V value) {

    }

    @Override
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
    }

    @Override
    public int compareTo(K k) {
        return 0;
    }

    @Override
    public Iterator<K> iterator() {
        return null;
    }
}
