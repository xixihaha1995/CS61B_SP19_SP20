package hw3.hash;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;

public class OomageTestUtility {
    public static boolean haveNiceHashCodeSpread(List<Oomage> oomages, int M) {
        /* TODO:
         * Write a utility function that returns true if the given oomages
         * have hashCodes that would distribute them fairly evenly across
         * M buckets. To do this, convert each oomage's hashcode in the
         * same way as in the visualizer, i.e. (& 0x7FFFFFFF) % M.
         * and ensure that no bucket has fewer than N / 50
         * Oomages and no bucket has more than N / 2.5 Oomages.
         */
        int N = oomages.size();
        int bucketNum;
        int[] bucket = new int[M];
        for (Oomage i : oomages) {
            bucketNum = (i.hashCode() & 0x7FFFFFFF) % M;
            bucket[bucketNum]++;
        }
        for (int i = 0; i < M; i++) {
            if (bucket[i] > N / 2.5 || bucket[i] < N / 50) {
                return false;
            }
        }
        return true;
    }



        /*int N = oomages.size();
        int bucketNum;
        Deque<Oomage>[] bucket =(Deque<Oomage> []) new Object[M];


        for (int i = 0; i < N; i++) {
            bucketNum = (oomages.get(i).hashCode() & 0x7FFFFFFF) % M;
            int loadFactor = bucket[bucketNum].size();
            if(loadFactor < N/2.5 && loadFactor > N/50) {
                bucket[bucketNum].add(oomages.get(i));
            } else {
                if(bucketNum==M-1){
                    bucketNum = -1;
                }
                bucket[bucketNum + 1].add(oomages.get(i));
            }

        }



    }*/
}
