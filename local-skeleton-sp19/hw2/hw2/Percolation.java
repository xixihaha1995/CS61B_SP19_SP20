package hw2;

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
//    public int[] block;
    public int open;
    public boolean[] markedOpen;
    public boolean[] markedFull;
    public int[] id;

    private int numberOfGrid;
    public Percolation(int N)                // create N-by-N grid, with all sites initially blocked
    {
        id = new int[ N * N ];
        numberOfGrid = N;
//        for (boolean b : markedFull[0]) {
//            markedFull[0][b] = true;
//        }
    }
    public void open(int row, int col)       // open the site (row, col) if it is not open already
    {
        validate(row, col);

        markedOpen[row][col] = true;
    }
    public boolean isOpen(int row, int col)  // is the site (row, col) open?
    {
        return markedOpen[row][col];
    }
    public boolean isFull(int row, int col)  // is the site (row, col) full?
    {
        return markedFull[row][col];
    }
    public int numberOfOpenSites()           // number of open sites
    {
        return open;
    }
    public boolean percolates()              // does the system percolate?
    {
        for ( boolean i: markedFull[numberOfGrid-1])
        {
            if ( markedFull[numberOfGrid-1][i])
            {
                return true;
            }
    }
        return false;
    }

    private int xyTo1D(int row, int col) {
        return row * col - 1;
    }
    private void validate ( int row, int col) {
        if ( row < 0 || row > numberOfGrid ) {
            throw new RuntimeException("Non-Valid Row Index");
        }
        if ( col < 0 || col > numberOfGrid ) {
            throw new RuntimeException("Non-Valid Col Index");
        }
    }

    public static void main(String[] args)   // use for unit testing (not required, but keep this here for the autograder)
}
