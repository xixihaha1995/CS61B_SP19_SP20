package bearmaps;

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;

/**
 * Created by hug. Demonstrates how you can use either
 * System.currentTimeMillis or the Princeton Stopwatch
 * class to time code.
 */
public class TimingTestDemo {
    public static void main(String[] args) {

//        ArrayHeapMinPQ<String> EPQ = new ArrayHeapMinPQ<>();
        //TODO make add call more efficient
        //Hungry
        ExtrnsicPQ<String> EPQ = new ExtrnsicPQ<>();
        Stopwatch sw = new Stopwatch();
        for (int i = 0; i < 1000000; i += 1) {
            EPQ.add("hi" + i,i+1);
        }
        System.out.println("Total epq add time elapsed: " + sw.elapsedTime() +  " seconds.");

        NaiveMinPQ<String> NAEPQ = new NaiveMinPQ<>();
        Stopwatch sw3 = new Stopwatch();
        for (int i = 0; i < 1000000; i += 1) {
            NAEPQ.add("hi" + i,i+1);
        }
        System.out.println("Total naive add time elapsed: " + sw3.elapsedTime() +  " seconds.");

        Stopwatch sw2 = new Stopwatch();
        for(int i = 0; i < 1000; i += 1) {
            int index = StdRandom.uniform(100000);
            EPQ.changePriority("hi" + index, index + 2);
        }

        System.out.println("Total time elapsed: " + sw2.elapsedTime() +  " seconds.");



        Stopwatch sw4 = new Stopwatch();
        for(int i = 0; i < 1000; i += 1) {
            int index = StdRandom.uniform(100000);
            NAEPQ.changePriority("hi" + index, index + 2);
        }

        System.out.println("Total time elapsed: " + sw4.elapsedTime() +  " seconds.");
    }
}
