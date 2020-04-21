public class ArrayDequeSizeTest {
    public static void main(String[] args) {
        ArrayDeque<Integer> lld1 = new ArrayDeque<Integer>();
        for(int i=0;i<11;i++){
            lld1.addFirst(i);
        }
        System.out.println(lld1.size());
        for(int i=0;i<11;i++){
            lld1.removeFirst();


        }
        System.out.println(lld1.size());
        for(int i=0;i<40;i++){
            lld1.addFirst(i);
        }
        System.out.println(lld1.size());
        for(int i=0;i<40;i++){
            lld1.removeFirst();
        }
        System.out.println(lld1.size());
    }
}
