package hw3.hash;

import edu.princeton.cs.algs4.StdRandom;

import java.util.ArrayList;
import java.util.List;

public class HashTableVisualizer {

    public static void main(String[] args) {
        /* scale: StdDraw scale
           N:     number of items
           M:     number of buckets */

        /* After getting your simpleOomages to spread out
           nicely, be sure to try
           scale = 0.5, N = 2000, M = 100. */

/*        double scale = 0.5;
        int N = 1000;
        int M = 256;

        HashTableDrawingUtility.setScale(scale);
        List<Oomage> oomies = new ArrayList<>();
        for (int i = 0; i < N; i += 1) {
//            oomies.add(SimpleOomage.randomSimpleOomage());
            oomies.add(ComplexOomage.randomComplexOomage());
        }
        visualize(oomies, M, scale);*/

        List<Oomage> deadlyList = new ArrayList<>();
        int N = 100;
        for (int i = 0; i < N; i += 1) {
            ArrayList<Integer> params = new ArrayList<>();
            params.add(StdRandom.uniform(1,255));
            for(int h =0;h<3;h++){
                params.add(1);
            }

            deadlyList.add(new ComplexOomage(params));
        }

        visualize(deadlyList, 10, 0.25);
    }

    public static void visualize(List<Oomage> oomages, int M, double scale) {
        HashTableDrawingUtility.drawLabels(M);
        int[] numInBucket = new int[M];
        for (Oomage s : oomages) {
            int bucketNumber = (s.hashCode() & 0x7FFFFFFF) % M;
            double x = HashTableDrawingUtility.xCoord(numInBucket[bucketNumber]);
            numInBucket[bucketNumber] += 1;
            double y = HashTableDrawingUtility.yCoord(bucketNumber, M);
            s.draw(x, y, scale);
        }
    }
} 
