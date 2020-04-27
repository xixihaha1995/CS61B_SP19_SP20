import static org.junit.Assert.*;
import org.junit.Test;
public class TestTOhex {
    @Test
    public void testToHex() {
        toHex th= new toHex(0);
        assertEquals(0, th);

        toHex th2= new toHex(-1);
        assertEquals("ffffffff", th2);

        toHex th3= new toHex(26);
        assertEquals("1a", th3);

    }

}
