import static org.junit.Assert.*;
import org.junit.Test;
public class TestArrayDequeGold {
    @Test
    public void testSADandADS(){
        StudentArrayDeque<Integer> sad1 = new StudentArrayDeque<>();
        ArrayDequeSolution<Integer> ads1 = new ArrayDequeSolution<>();

        for (int i = 0; i < 10; i += 1) {
            double numberBetweenZeroAndOne = StdRandom.uniform();

            if (numberBetweenZeroAndOne < 0.5) {
                sad1.addLast(i);
                ads1.addLast(i);
            } else {
                if ( sad1.size() > 0 && ads1.size() > 0 ) {
                    sad1.removeFirst();
                    ads1.removeFirst();
                }

            }
        }
        for (int i = 0; i < 10; i += 1) {
            double numberBetweenZeroAndOne = StdRandom.uniform();

            if (numberBetweenZeroAndOne < 0.5) {
                assertEquals("random",ads1.get(i), sad1.get(i));
            } else {
                assertEquals("random",ads1.get(i), sad1.get(i));
            }
        }


    }
}
