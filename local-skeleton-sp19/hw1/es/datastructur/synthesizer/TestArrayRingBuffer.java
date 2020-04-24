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
        Double exp = 33.1;
//        assertEquals(exp, x.dequeue());
        x.enqueue(33.1) ;// 33.1 null null  null
        x.enqueue(44.8) ;// 33.1 44.8 null  null
        x.enqueue(62.3) ;// 33.1 44.8 62.3  null
        x.enqueue(-3.4) ;// 33.1 44.8 62.3 -3.4
        Double front  = x.dequeue();     // 44.8 62.3 -3.4  null (returns 33.1)
//        Double exp = 33.1;
        Double exp2 = 44.8;
        assertEquals(exp, front);

        assertEquals(exp, x.peek());
        assertEquals(exp, x.dequeue());
        assertFalse(x.isEmpty());

    }
}
