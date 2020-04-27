  
public class max {
   public static int max(int[] m) {
      int maxIndex = 0;
      int l = m.length;
      for (int p = 0; p < l; p +=1){
         if (m[p] > m[maxIndex]){
            maxIndex = p;
         }
      }
      return m[maxIndex];
   }
   public static void main(String[] args) {
      int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
      System.out.println(max(numbers));
   }
}
