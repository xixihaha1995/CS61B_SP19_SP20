import static org.junit.Assert.*;
import org.junit.Test;

public class DequeTest {
    @Test
    public void testAddFirst(){
        String input = "cat";
        Deque<String> deque = new Deque<String>();
        deque.addFirst(input);
        assertArrayEquals(input,deque);
    }

}
