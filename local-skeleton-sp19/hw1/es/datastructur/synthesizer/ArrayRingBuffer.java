package es.datastructur.synthesizer;
//TODO: Make sure to that this class and all of its methods are public
//TODO: Make sure to add the override tag for all overridden methods
//TODO: Make sure to make this class implement BoundedQueue<T>

import java.util.Iterator;

public class ArrayRingBuffer<T> implements BoundedQueue<T> {
    /* Index for the next dequeue or peek. */
    private int first;
    /* Index for the next enqueue. */
    private int last;
    /* Variable for the fillCount. */
    private int fillCount;
    /* Array for storing the buffer data. */
    private T[] rb;

    private int bufferCapacity;



    /**
     * Create a new ArrayRingBuffer with the given capacity.
     */
    public ArrayRingBuffer(int capacity) {
        // TODO: Create new array with capacity elements.
        //       first, last, and fillCount should all be set to 0.
        bufferCapacity = capacity;
        rb = (T []) new Object[capacity];
        first = 0;
        last  = 0;
        fillCount = 0;
    }


    /**
     * Adds x to the end of the ring buffer. If there is no room, then
     * throw new RuntimeException("Ring buffer overflow").
     */
    public int fillCount() {
        return fillCount;
    }
    public int capacity() {
        return bufferCapacity;
    }
    public void enqueue(T x) {
        // TODO: Enqueue the item. Don't forget to increase fillCount and update
        //       last.
        if ( isFull() ) {
            throw new RuntimeException("Ring buffer overflow");
        }
        rb[last ] = x;
        fillCount += 1;
        last =circular(last +1);
    }

    /**
     * Dequeue oldest item in the ring buffer. If the buffer is empty, then
     * throw new RuntimeException("Ring buffer underflow").
     */
    public T dequeue() {
        // TODO: Dequeue the first item. Don't forget to decrease fillCount and
        //       update first.
        if ( isEmpty() ) {
            throw new RuntimeException("Ring buffer underflow");
        } else {
            T returnItem = rb[first];
            first =circular(first +1);
            fillCount -= 1;
            return returnItem;
           /* int p = first;
            T sto = rb[circular(first)];
            for (int i = 0; i < fillCount - 1; i++) {
                rb[ circular(p) ] = rb[ circular(p++) ];
            }
            rb[ circular(p) ] = null;
            first -= 1;
            fillCount -= 1;

            return sto;
*/
        }

    }

    /**
     * Return oldest item, but don't remove it. If the buffer is empty, then
     * throw new RuntimeException("Ring buffer underflow").
     */
    public T peek() {
        // TODO: Return the first item. None of your instance variables should
        //       change.
        if ( isEmpty() ) {
            throw new RuntimeException("Ring buffer underflow");
        }
        return rb[ first ];
    }
    private int circular (int i) {
        if ( i > bufferCapacity || i == bufferCapacity ) {
            return i - bufferCapacity;
        } else {
/*            if ( i < 0 ) {
                return  i + bufferCapacity;
            }*/
            return i;
        }
    }

    private Iterator<T> ARBiterator() implements Iterator<T> {
        private int wizPos;
        public ARBiterator() { wizPos = 0; }
        public boolean hasNext() { return wizPos < fillCount; }
        public T next() {
            T returnItem = rb[wizPos];
            wizPos += 1;
            return (Iterator<T>) returnItem;
        }
    }
    @Override
    public boolean equals(Object o) {
        if ( o == null) { return false;}
        if ( this.getClass() != o.getClass()) { return false;}
        ArrayRingBuffer<T> other = ( ArrayRingBuffer<T>) o;
        if ( this.fillCount() != other.fillCount() ) { return false;}
/*        for ( T i : other) {
            if ( true ) {
                return false;
            }
        }*/
        return true;
    }



//    public Iterator<T> ARBIterator<T>(){
//        return Iterator<T>;
//    }

//    private String toString() {
//
//    }

    // TODO: When you get to part 4, implement the needed code to support
    //       iteration and equals.
}
    // TODO: Remove all comments that say TODO when you're done.
