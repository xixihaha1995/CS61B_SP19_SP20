package es.datastructur.synthesizer;
import java.util.Iterator;

//TODO: Make sure to that this class and all of its methods are public
//TODO: Make sure to add the override tag for all overridden methods
//TODO: Make sure to make this class implement BoundedQueue<T>

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

    public T[] items;

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
            throw new RuntimeException("This ARB is full");
        }
        rb[ circular(last) ] = x;
        fillCount += 1;
        last += 1;
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
            int p = first;
            T sto = rb[circular(first)];
            for (int i = 0; i < fillCount - 1; i++) {
                rb[ circular(p) ] = rb[ circular(p++) ];
            }
            rb[ circular(p) ] = null;
            last -= 1;
            fillCount -= 1;

            return sto;

        }

    }

    /**
     * Return oldest item, but don't remove it. If the buffer is empty, then
     * throw new RuntimeException("Ring buffer underflow").
     */
    public T peek() {
        // TODO: Return the first item. None of your instance variables should
        //       change.
        return rb[ circular(first) ];
    }
    private int circular (int i) {
        if ( i >= bufferCapacity ) {
            return i - bufferCapacity;
        } else {
            return i;
        }
    }

    // TODO: When you get to part 4, implement the needed code to support
    //       iteration and equals.
}
    // TODO: Remove all comments that say TODO when you're done.
