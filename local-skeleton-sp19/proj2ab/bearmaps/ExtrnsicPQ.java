package bearmaps;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class ExtrnsicPQ<T> implements ExtrinsicMinPQ<T> {


    @Override
    public void add(T item, double priority) {
        if (setForKeys.contains(item)) {
            throw new IllegalArgumentException;
        }
        fakeTree.add(new Entry(item,priority));

        size += 1;
        setForKeys.add(item);
    }
    private void swim(Entry<T> entry) {

    }
    private int parent (int index) {
        if (index % 2 ==0) {
            return index / 2;
        } else {
            return (index -1)/2;
        }
    }
    private void swap(Entry<T> entryA, Entry<T> entryB) {

    }


    @Override
    public boolean contains(T item) {
        return false;
    }

    @Override
    public T getSmallest() {
        return null;
    }

    @Override
    public T removeSmallest() {
        return null;
    }

    @Override
    public int size() {
        return 0;
    }

    @Override
    public void changePriority(T item, double priority) {

    }



    private Set<T> setForKeys;
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
        size = 0;
        fakeTree = new ArrayList<Entry<T>>();
        Entry<T> sentinel;
        sentinel = new Entry("random", 2.5);
        fakeTree.add(sentinel);
    }

    //    private tree root;

/*    private class tree<T>{

        tree left;
        tree right;
        T key;
        int index;
        double priority;

        public tree(T item, double weight, tree left, tree right) {
            key = item;
            priority = weight;
            this.left = left;
            this.right = right;
        }
        public T parent(T item) {

        }

    }*/
}
