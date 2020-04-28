import static org.junit.Assert.*;
import org.junit.Test;

public class SolutionTester {
    @Test
    public void testMergeInter() {
        int[][] inp = new int[][]{
                {1,3},{2,6},{8,10},{15,18}
        };
        int[][] exp = new int[][]{
                {1,6},{8,10},{15,18}
        };
        assertEquals(exp, MergeInter.mergeInter(inp));
    }
/*    @Test
    public void testSearchRo() {
*//*        int[] nums = new int[]{2,5,6,0,0,1,2};
        assertTrue(searchRo.search(nums, 0));
        assertFalse(searchRo.search(nums,3));*//*
        int[] nums2 = new int[]{1,1};
//        assertFalse(searchRo.search(nums2,0));
        assertFalse(searchRo.search(nums2,2));
    }*/
}
