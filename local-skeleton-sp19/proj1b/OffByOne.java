public class OffByOne implements CharacterComparator{
    @Override
    boolean equalChars(char x, char y) {
        if (Math.abs((int) (x - y)) == 1) {
            return true;
        } else {
            return false;
        }
    }

}
