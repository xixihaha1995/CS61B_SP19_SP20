package es.datastructur.synthesizer;


public class ARBIterator<T> implements Iterator<T> {
    private int wizPos;
    public ARBIterator() { wizPos = 0; }
    public boolean hasNext() { return wizPos < .size; }
    public T next() {
        T returnItem = rb[wizPos];
        wizPos += 1;
        return returnItem;
    }
}
