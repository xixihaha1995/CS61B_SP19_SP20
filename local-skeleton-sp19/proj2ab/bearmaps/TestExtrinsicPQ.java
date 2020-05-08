package bearmaps;
import static org.junit.Assert.*;
import org.junit.Test;

public class TestExtrinsicPQ {
/*    @Test
    public void testAdd(){
        ExtrnsicPQ<Character> EPQ = new ExtrnsicPQ<>();
        EPQ.add('c',3.5);
        EPQ.add('d',5.3);
        EPQ.add('e',0.3);
        EPQ.add('a',-0.3);
    }

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
        EPQ.add('d',3.5);
        EPQ.removeSmallest();
    }

    @Test
    public void testChangePriority() {
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        EPQ.add("cat",3.5);
        EPQ.changePriority("cat",7.0);
    }*/
    @Test
    public void TestgetSmallest() {
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        EPQ.add("cat",0.1);
        EPQ.add("dog",2);
        EPQ.changePriority("cat",3.0);
        EPQ.changePriority("dog",4.0);
        EPQ.changePriority("cat",7);
        assertEquals("dog",EPQ.getSmallest());
    }
}
