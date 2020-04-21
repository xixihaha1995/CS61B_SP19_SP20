import static org.junit.Assert.*;

import org.junit.Test;

public class FlikTest{
	@Test
	public void testSame(){
		int i = 127;
		int j = 127;
		assertTrue(Flik.isSameNumber(i,j));
		i = 128;
		j = 128;
		assertTrue(Flik.isSameNumber(i,j));
	}
}