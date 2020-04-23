package es.datastructur.synthesizer;
import org.junit.Test;
import static org.junit.Assert.*;

/** Tests the ArrayRingBuffer class.
 *  @author Josh Hug
 */

public class TestArrayRingBuffer {
    @Test
    public void someTest() {
        ArrayRingBuffer<Double> x = new ArrayRingBuffer(10);

        x.enqueue(33.1) ;// 33.1 null null  null
        x.enqueue(44.8) ;// 33.1 44.8 null  null
        x.enqueue(62.3) ;// 33.1 44.8 62.3  null
        x.enqueue(-3.4) ;// 33.1 44.8 62.3 -3.4
        Double front  = x.dequeue();     // 44.8 62.3 -3.4  null (returns 33.1)
        assertEquals(java.util.Optional.of(33.1), front);
        assertEquals(java.util.Optional.of(44.8), x.peek());
        assertEquals(java.util.Optional.of(44.8), x.dequeue());
        assertFalse(x.isEmpty());

    }
}
