package bearmaps;

import edu.princeton.cs.algs4.In;

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
        temIndex = size + 1;
        indexForKeys.put(item,temIndex);
        if ( size > 0 ) {
            fakeTree.get(temIndex);
            swim(fakeTree.get(temIndex));
            size += 1;
            setForKeys.add(item);
//            indexForKeys.put(item,temIndex);
        } else {
            size += 1;
            setForKeys.add(item);
            indexForKeys.put(item,1);
        }





        //simply get the curEntry index and put it in HashMap

    }
    private void swim(Entry<T> entry) {

        int curInd = indexForKeys.get(entry.key);
        if( parent(curInd) !=null ){
            if (parent(curInd)>0){
                Entry<T> parentEntry = fakeTree.get(parent(curInd));
                if ( parentEntry.priority > entry.priority ) {
                    swap (entry, parentEntry);
                    swim(parentEntry);
                }
            }
        }



    }

    private Integer parent (int curIndex) {

        if (curIndex % 2 ==0) {
            if(curIndex / 2 >0){
                return temIndex = curIndex / 2;
            }

        } else {
            if( (curIndex - 1) / 2 > 0){
                return temIndex = (curIndex - 1) / 2;
            }

        }
        temIndex = temIndex > 0 ? temIndex: null ;
        return null;


    }

    private void swap(Entry<T> entryA, Entry<T> entryB) {
        T tempKey;
        double tempPriority;
        int temIndex;

        tempKey = entryA.key;
        tempPriority = entryA.priority;
        temIndex = indexForKeys.get(entryA.key);
        int entryBIndex = indexForKeys.get(entryB.key);

        entryA.key = entryB.key;
        entryA.priority = entryB.priority;

        indexForKeys.replace(entryB.key,temIndex);
        entryB.key = tempKey;
        entryB.priority = tempPriority;
        indexForKeys.replace(entryB.key,entryBIndex);
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
        Integer childIndex = smallerChild(curIndex);
        if( childIndex !=null ){
            Entry<T> childEntry = fakeTree.get(childIndex);
            if ( childEntry.priority < entry.priority ) {
                swap (entry, childEntry);
                sink(childEntry);
            }
        }



    }
    private Integer smallerChild (int entryIndex) {
        int returnIndex;
        Integer leftIndex = leftChild(entryIndex);
        Integer rightIndex = rightChild(entryIndex);
        if (leftIndex !=null && rightIndex != null) {
            if (fakeTree.get(leftIndex).priority <= fakeTree.get(rightIndex).priority) {
                return leftIndex;
            } else {
                return rightIndex;
            }
        } else {
            if(leftIndex != null) {
                return leftIndex;
            }
            return null;
        }

    }
    private Integer leftChild (int entryIndex) {
        return (entryIndex * 2 > size ) ? null: entryIndex * 2;
    }
    private Integer rightChild (int entryIndex) {
        return ( entryIndex * 2 + 1 > size ) ? null: entryIndex * 2;
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
        swim(curEntry);
        sink(curEntry);
//        indexForKeys.replace(item,temIndex);
    }



    private Set<T> setForKeys;
    private HashMap<T,Integer> indexForKeys;
    private int size;
    private int temIndex;
    private int temSinkIndex;
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
/*        Entry<T> sentinel;
        sentinel = new Entry("random", 0);*/
        fakeTree.add(null);
        temIndex = 0;
    }

}
