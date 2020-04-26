package hw2;

public class Percolation {
//    public int[] block;
    public int open;
    public boolean[] markedOpen;
    public boolean[] markedFull;
    public int[] parent;
    private int[] size;
    private int[] surSize;

    private int numberOfGrid;
    public Percolation(int N)                // create N-by-N grid, with all sites initially blocked
    {
        int cap = N * N;
        numberOfGrid = N;
        open = 0;
        parent = new int[ cap ];
        size = new int[cap];
        markedFull = new boolean[cap];
        markedOpen = new boolean[cap];
        for (int i = 0; i < cap; i++) {
            markedOpen[i] = false;
            markedFull[i] = false;
            size[i] = 1;
            surSize[i] = 0;
        }
    }

//        for (boolean b : markedFull[0]) {
//            markedFull[0][b] = true;
//        }
    }
    public int open(int row, int col)       // open the site (row, col) if it is not open already
    {
        validate(row, col);
        if ( ! isOpen( row, col )) {
            markedOpen[xyTo1D(row, col)] = true;
            open += 1;
            //TODO search for the surrounding to see if there are open sites
            surrounding(row, col);
        }
    }
    private void surrounding(int curRow, int curCol) {
        valiSur(curRow, curCol, curRow - 1, curCol);
        valiSur(curRow, curCol, curRow + 1, curCol);
        valiSur(curRow, curCol, curRow , curCol - 1);
        valiSur(curRow, curCol, curRow, curCol + 1);
    }
    private void valiSur(int curRow, int curCol, int rowTa, int colTa) {
    if (validNoException(rowTa,colTa) ]) {
        if ( markedOpen[xyTo1D(rowTa, colTa)) {
            union(xyTo1D(curRow,curCol),xyTo1D(rowTa, colTa));
        }
    }
    }
    private boolean validNoException(int row, int col) {
        if ( row < 0 || row > numberOfGrid || col < 0 || col > numberOfGrid) {
            return false;
        } else {
            return true;
        }

    }


    public boolean isOpen(int row, int col)  // is the site (row, col) open?
    {
        return markedOpen[xyTo1D(row, col)];
    }
    public boolean isFull(int row, int col)  // is the site (row, col) full?
    {
        return markedFull[xyTo1D(row, col)] ;
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
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;

        // make smaller root point to larger one
        if (size[rootP] < size[rootQ]) {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        else {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        }

    }

    private int xyTo1D(int row, int col){
        validate(row, col);
        return row * numberOfGrid + col;
    }
    private void validate ( int row, int col) {
        if ( row < 0 || row > numberOfGrid ) {
            throw new RuntimeException("Non-Valid Row Index");
        }
        if ( col < 0 || col > numberOfGrid ) {
            throw new RuntimeException("Non-Valid Col Index");
        }
    }
    public int find(int p){
        validate(p);
        while (p != parent[p])
            p = parent[p];
        return p;
    }
    public boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    public static void main(String[] args)   // use for unit testing (not required, but keep this here for the autograder)
}
