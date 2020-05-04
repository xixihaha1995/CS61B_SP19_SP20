import java.util.*;

public class MyHashMap<K,V> implements Map61B<K,V> {
    private int sizeNum;
    public Set<K> setForKeys;
    private int initialSize;
    private double loadFactor;
//    private int buckNum;
    private ArrayList<K> bucket;

    public MyHashMap(){
        this.initialSize = 16;
        this.loadFactor = 0.75;
        bucket.set()
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
            ArrayDeque<K> curArray = bucket[buckNum];
            curArray.add(key);
            curArray[key].element() = value;
            setForKeys.add(key);
        }

    }
    private  class naiveHashMap{
        K keyNaive;
        V valueNaive;
        int sizeNaive;
        public naiveHashMap(K key, V value){
            keyNaive = key;
            valueNaive = value;
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

