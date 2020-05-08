package bearmaps;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class ExtrnsicPQ<T> implements ExtrinsicMinPQ<T> {


    @Override
    public void add(T item, double priority) {
/*        if (setForKeys.contains(item)) {
            throw new IllegalArgumentException("Key already existed");
        }*/

        Entry<T> curEntry = new Entry(item,priority);

        fakeTree.add(new Entry(item,priority));
        size += 1;
        swim(fakeTree.get(size));
        setForKeys.add(item);
        indexForKeys.put(item,fakeTree.indexOf(curEntry));
    }
    private void swim(Entry<T> entry) {
        if ( parent(entry).priority > entry.priority ) {
            swap (entry, parent(entry));
            /* TODO swim(parent(entry)) or swim(entry) */
            swim(parent(entry));
        }

    }

    private Entry<T> parent (Entry<T> entry) {
        if (fakeTree.indexOf(entry) % 2 ==0) {
            return fakeTree.get(fakeTree.indexOf(entry) / 2);

        } else {
            return fakeTree.get((fakeTree.indexOf(entry) - 1) / 2) ;
        }
    }

    private void swap(Entry<T> entryA, Entry<T> entryB) {
        T tempKey;
        double tempPriority;

        tempKey = entryA.key;
        tempPriority = entryA.priority;
        entryA.key = entryB.key;
        entryA.priority = entryB.priority;
        entryB.key = tempKey;
        entryB.priority = tempPriority;
    }


    @Override
    public boolean contains(T item) {
        return setForKeys.contains(item);

    }

    @Override
    public T getSmallest() {
        return fakeTree.get(1).key;
    }

    @Override
    public T removeSmallest() {
        T returnT = fakeTree.get(1).key;
        size -= 1;
        setForKeys.remove(returnT);

        fakeTree.remove(1);
        if (size > 0) {
            Entry<T> lastEntry = fakeTree.get(fakeTree.size()-1);
            Entry<T> tempEntry = new Entry(lastEntry.key,lastEntry.priority);
            fakeTree.set(1,tempEntry);
            sink(fakeTree.get(1));
        }

        return returnT;
    }

    private void sink(Entry<T> entry) {
        Entry<T> childEntry = smallerChild(entry);
        if ( childEntry.priority < entry.priority ) {
            swap (entry, childEntry);
            sink(smallerChild(entry));
        }

    }
    private Entry<T> smallerChild (Entry<T> entry) {
        Entry<T> returnEntry;
        if (leftChild(entry).priority <= rightChild(entry).priority) {
            return leftChild(entry);
        } else {
            return rightChild(entry);
        }
    }
    private Entry<T> leftChild (Entry<T> entry) {
        int leftChildIndex = fakeTree.indexOf(entry) * 2;
        return fakeTree.get(leftChildIndex);
    }
    private Entry<T> rightChild (Entry<T> entry) {
        int rightChildIndex = fakeTree.indexOf(entry) * 2 + 1;
        return fakeTree.get(rightChildIndex);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void changePriority(T item, double updatedPriority) {
        //TODO from O(N) to O(log N)
        //modify your addForChangingPriority
/*        if ( !contains(item) ){
            throw new IllegalArgumentException("Key not existed");
        }*/
        Entry<T> curEntry = fakeTree.get(indexForKeys.get(item));
        curEntry.priority = updatedPriority;

/*        for( Entry<T> i: fakeTree){
            if(item == i.key){
                i.priority = priority;
                break;
            }
        }*/
    }



    private Set<T> setForKeys;
    private HashMap<T,Integer> indexForKeys;
    private int size;
    private ArrayList<Entry<T>> fakeTree;
    private class Entry<T>{
        T key;
        double priority;
        public Entry(T key, double priority) {
            this.key = key;
            this.priority = priority;
        }
    }

    //TODO constructor for ExtrnsicPQ
    //fakeTree is leaving one empty spot tree
    public ExtrnsicPQ(){
        setForKeys = new HashSet<T>();
        indexForKeys = new HashMap<>();
        size = 0;
        fakeTree = new ArrayList<Entry<T>>();
        Entry<T> sentinel;
        sentinel = new Entry("random", 2.5);
        fakeTree.add(sentinel);
    }

}
