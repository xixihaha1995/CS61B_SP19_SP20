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

        fakeTree.add(curEntry);
        if ( size > 0 ) {
            swim(fakeTree.get(size));
            size += 1;
            setForKeys.add(item);
            indexForKeys.put(item,temIndex);
        } else {
            size += 1;
            setForKeys.add(item);
            indexForKeys.put(item,1);
        }





        //simply get the curEntry index and put it in HashMap

    }
    private void swim(Entry<T> entry) {

        int curInd = indexForKeys.get(entry.key);
        Entry<T> parentEntry = fakeTree.get(parent(curInd));
        if ( parentEntry.priority > entry.priority ) {
            swap (entry, parentEntry);
            swim(parentEntry);
        }

    }

    private int parent (int curIndex) {

        if (curIndex % 2 ==0) {
            temIndex = curIndex / 2;
        } else {
            temIndex = (curIndex - 1) / 2;
        }
        return temIndex;
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
        int curIndex = indexForKeys.get(entry.key);
        int childIndex = smallerChild(curIndex);

        Entry<T> childEntry = fakeTree.get(childIndex);
        if ( childEntry.priority < entry.priority ) {
            swap (entry, childEntry);
            sink(childEntry);
        }

    }
    private int smallerChild (int entryIndex) {
        int returnIndex;
        int leftIndex = leftChild(entryIndex);
        int rightIndex = rightChild(entryIndex);
        if (fakeTree.get(leftIndex).priority <= fakeTree.get(rightIndex).priority) {
            return leftIndex;
        } else {
            return rightIndex;
        }
    }
    private int leftChild (int entryIndex) {
        return entryIndex * 2;
    }
    private int rightChild (int entryIndex) {
        return entryIndex * 2 + 1;
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

        int curIndex = indexForKeys.get(item);
        Entry<T> curEntry = fakeTree.get(curIndex);
        curEntry.priority = updatedPriority;
        int parentIndex = parent(curIndex);
        if(fakeTree.get(parentIndex).priority < curEntry.priority) {
            swim(curEntry);
        }
        int childIndex = smallerChild(curIndex);
        Entry<T> childEntry = fakeTree.get(childIndex);
        if (childEntry.priority < curEntry.priority) {
            sink(curEntry);
        }
        //TODO swim or sink

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
    private int temIndex;
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
        temIndex = 0;
    }

}
