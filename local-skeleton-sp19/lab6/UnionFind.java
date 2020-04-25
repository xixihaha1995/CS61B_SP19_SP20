public class UnionFind {
    public int[] id;
    public int[] size;
    private int[] root;
    public boolean[] marked;
    private int numberOfVertices;

    // TODO - Add instance variables?

    /* Creates a UnionFind data structure holding n vertices. Initially, all
       vertices are in disjoint sets. */
    public UnionFind(int n) {
        numberOfVertices = n;
        id = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
            root[i] = i;
            size[i] = 1;

        }
        // TODO
    }

    /* Throws an exception if v1 is not a valid index. */
    private void validate(int vertex) {
        if ( vertex < 0 || vertex >= numberOfVertices) {
            throw new RuntimeException("Valid indxe");
        }
        // TODO
    }

    /* Returns the size of the set v1 belongs to. */
    public int sizeOf(int v1) {
        // TODO
        validate(v1);
        return size[v1];
    }

    /* Returns the parent of v1. If v1 is the root of a tree, returns the
       negative size of the tree for which v1 is the root. */
    public int parent(int v1) {
        // TODO
        validate(v1);
        if ( find(v1) == v1) {
            return -1 * sizeOf(v1);
        }

        return id[v1];
    }
/*    private int root(int v1) {
        //TODO path compression
        while ( id[v1] != v1) {
            id[v1] = id[id[v1]];
        }
        return id[v1];
    }*/

    /* Returns true if nodes v1 and v2 are connected. */
    public boolean connected(int v1, int v2) {
        // TODO
        validate(v1);
        validate(v2);
        if ( root[v1] == root[v2]) {
            return true;
        } else {
            return false;
        }

    }

    /* Connects two elements v1 and v2 together. v1 and v2 can be any valid 
       elements, and a union-by-size heuristic is used. If the sizes of the sets
       are equal, tie break by connecting v1's root to v2's root. Unioning a 
       vertex with itself or vertices that are already connected should not 
       change the sets but may alter the internal structure of the data. */
    public void union(int v1, int v2) {
        // TODO
        validate(v1);
        validate(v2);
        int rootOne = find(v1);
        int rootTwo = find(v2);
        if ( sizeOf(v1) > sizeOf(v2)) {
            find(v2) = rootOne;
            sizeOf(v1) += sizeOf(v2);
        }
        if ( sizeOf(v1) < sizeOf(v2)) {
            find(v1) = rootOne;
            sizeOf(v2) += sizeOf(v1);
        }


        }
    }

    /* Returns the root of the set V belongs to. Path-compression is employed
       allowing for fast search-time. */
    public int find(int v1) {
        //TODO path compression
        validate(v1);
        while ( id[v1] != v1) {
            id[v1] = id[id[v1]];
        }
        return id[v1];
    }

}
