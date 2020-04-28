import static org.junit.Assert.*;
import org.junit.Test;

public class SolutionTester {
    @Test
    public void testSomething() {
        int[] nums = new int[]{2,5,6,0,0,1,2};
        assertTrue(searchRo.search(nums, 0));
        assertFalse(searchRo.search(nums,3));
    }
}
