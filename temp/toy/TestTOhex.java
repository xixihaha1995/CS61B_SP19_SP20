import static org.junit.Assert.*;
import org.junit.Test;
public class TestTOhex {
    @Test
    public void testToHex() {

        assertEquals("ffffffff", convertToHex.toHex(-1));
        assertEquals("1a", convertToHex.toHex(26));

/*        toHex th2= new toHex(-1);
        assertEquals("ffffffff", th2);

        toHex th3= new toHex(26);
        assertEquals("1a", th3);*/

    }

}
