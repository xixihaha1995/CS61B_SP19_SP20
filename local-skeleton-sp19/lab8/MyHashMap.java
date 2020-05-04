import java.util.*;

public class MyHashMap<K,V> implements Map61B<K,V> {
    private int sizeNum;
    public Set<K> setForKeys;
    private int initialSize;
    private double loadFactor;
//    private int buckNum;
    private ArrayList<Entry<K,V>> bucket;

    public MyHashMap(){
        this.initialSize = 16;
        this.loadFactor = 0.75;
        bucket = new ArrayList<Entry<K,V>>(initialSize);
        bucket.addAll (Collections.nCopies (initialSize, null));
        sizeNum = 0;
        setForKeys = new HashSet<K>();
    }
    public MyHashMap(int initialSize){}
    public MyHashMap(int initialSize, double loadFactor){}


    @Override
    public void clear() {
        setForKeys = new HashSet<K>();
        sizeNum = 0;
        bucket.addAll (Collections.nCopies (initialSize, null));
//        bucket = null;
    }

    @Override
    public boolean containsKey(K key) {
        if (setForKeys == null) {
            return false;
        } else {
            return setForKeys.contains(key);
        }

    }
    @Override
    public void put(K key, V value) {


        int h = hash (key);
        Entry<K,V> e = find (key, bucket.get (h));
        if (e == null) {
            bucket.set (h, new Entry<K,V> (key, value, bucket.get(h)));
            sizeNum += 1;
            setForKeys.add(key);
        }


    }
    private int hash(Object key) {
        return  (key == null) ? 0
                : (0x7fffffff & key.hashCode ()) % curBucketSize() ;
    }
    private int curBucketSize(){
        return initialSize;
    }
    private static class Entry<K,V>{
        K keyNaive;
        V valueNaive;
        Entry<K, V> next;
        public Entry(K key, V value, Entry<K,V> next){
            this.keyNaive = key;
            this.valueNaive = value;
            this.next = next;
        }
        public V setValue (V x) {
            V old = valueNaive;
            valueNaive = x;
            return old;
        }

    }
    private Entry<K,V> find (Object key, Entry<K,V> bin) {
        for (Entry<K,V> e = bin; e != null; e = e.next)
            if (key == null && e.keyNaive == null || key.equals (e.keyNaive))
                return e;
        return null;
    }



    @Override
    public V get(Object key) {
        Entry<K,V> e = find(key, bucket.get(hash(key)));
        return (e == null) ? null : e.valueNaive;
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

