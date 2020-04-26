package hw2;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;

public class PercolationStats {

    public double[] fraction;
    public double meanCur;
    public int grid;
    public int time;
    public PercolationStats(int N, int T, PercolationFactory pf){
        fraction = new double[T];
        time = T;
        grid = N;
        for (int i = 0; i < T; i++) {
            Percolation pfCur = pf.make(N);
            while(!pfCur.percolates()) {
                pfCur.open(StdRandom.uniform(N),StdRandom.uniform(N));
            }
            fraction[i] = pfCur.numberOfOpenSites()/(1.0*N*N);

        }
    }   // perform T independent experiments on an N-by-N grid
    public double mean() {
        meanCur = 0.0;
        for(int i = 0; i < time; i++) {
            meanCur = meanCur + fraction[i];
        }
        return meanCur/time;
    }                                   // sample mean of percolation threshold
 /*   public double stddev()                                         // sample standard deviation of percolation threshold
    public double confidenceLow()                                  // low endpoint of 95% confidence interval
    public double confidenceHigh()                                 // high endpoint of 95% confidence interval
    */
    public static void main(String[] args) {
        Stopwatch timer1 = new Stopwatch();
        PercolationFactory pf = new PercolationFactory();
        int timeNum = 5;
        double[] time = new double[timeNum];
        double[] mean = new double[timeNum];
        for(int i=0;i<timeNum;i++){
            PercolationStats ps = new PercolationStats(20,30*(i+1),pf);
            mean[i] = ps.mean();
            time[i] = timer1.elapsedTime();
        }
        for(int i=0; i<timeNum;i++){
            System.out.println("%.2f (%.2f seconds)", mean[i], time[i]);
        }



    }
}