package es.datastructur.synthesizer;

import java.util.Iterator;


private java.util.Iterator<T> ARBiterator() implements Iterator<T>{
    private int wizPos;
    public iterator() { wizPos = 0; }
    public boolean hasNext() { return wizPos < fillCount; }
    public T next() {
        T returnItem = rb[wizPos];
        wizPos += 1;
        return (Iterator<T>) returnItem;
    }
}