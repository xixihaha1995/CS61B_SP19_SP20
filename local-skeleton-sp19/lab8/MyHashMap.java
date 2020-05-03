import java.util.Deque;
import java.util.Iterator;
import java.util.Set;

public class MyHashMap<K,V> implements Map61B<K,V> {
    private int sizeNum;
    public Set<K> setForKeys;
    private int initialSize;
    private double loadFactor;
//    private int buckNum;
    private Deque<K>[] bucket;

    public MyHashMap(){
        this.initialSize = 16;
        this.loadFactor = 0.75;
        bucket = (Deque<K> []) new Object[initialSize];
    }
    public MyHashMap(int initialSize){}
    public MyHashMap(int initialSize, double loadFactor){}


    @Override
    public void clear() {
        setForKeys = null;
        sizeNum = 0;
    }

    @Override
    public boolean containsKey(K key) {
        return setForKeys.contains(key);
    }
    @Override
    public void put(K key, V value) {
        int curHash = key.hashCode();
        int buckNum = ( curHash & 0x7FFFFFFF) % initialSize;
        double curLoadFactor = bucket[buckNum].size()*1.0/sizeNum;
        if (curLoadFactor < loadFactor) {
            bucket[buckNum].
        }

    }

    @Override
    public V get(K key) {
        return null;
    }

    @Override
    public int size() {
        return sizeNum;
    }



    @Override
    public Set<K> keySet() {

        return setForKeys;
    }

    @Override
    public Iterator<K> iterator() {
        return null;
    }



    @Override
    public V remove(K key) {
        throw new UnsupportedOperationException();
    }

    @Override
    public V remove(K key, V value) {
        throw new UnsupportedOperationException();
    }

}

