public class OffByN implements CharacterComparator{
    public int N;

    public OffByN(int n){
        N = n;
    }
    @Override
    public boolean equalChars(char x, char y){
        if (Math.abs((int) (x - y)) == N) {
            return true;
        } else {
            return false;
        }
    }

}
