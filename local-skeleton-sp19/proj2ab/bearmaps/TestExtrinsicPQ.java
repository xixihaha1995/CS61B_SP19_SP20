package bearmaps;
import static org.junit.Assert.*;
import org.junit.Test;

public class TestExtrinsicPQ {
    @Test
    public void testAdd(){
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        EPQ.add("cat",3.5);
        EPQ.add("bigCat",5.3);
    }
/*
   @Test
    public void testAddContainSize(){
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        EPQ.add("cat",3.5);
        assertTrue(EPQ.contains("cat"));
        EPQ.add("dog",5.0);
        assertEquals(2,EPQ.size());
       EPQ.add("mouse",5.0);
       assertEquals(3,EPQ.size());
    }

    @Test
    public void testAddRemove(){
        ExtrnsicPQ<Character> EPQ = new ExtrnsicPQ<>();
        EPQ.add('c',3.5);
        EPQ.removeSmallest();
        EPQ.add(65,3.5);
        EPQ.removeSmallest();
    }

    @Test
    public void testChangePriority() {
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        EPQ.add("cat",3.5);
        EPQ.changePriority("cat",7.0);
    }
    @Test
    public void TestgetSmallest() {
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        EPQ.add("cat",3.5);
        EPQ.add("dog",5);
        EPQ.changePriority("cat",7.0);
    }*/
}
