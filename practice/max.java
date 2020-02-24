public class ClassNameHere {
   public static int max(int[] m) {
      int maxIndex = 0;
      int p = 0;
      int l = m.length;
      while(p < l){  
         if (m[p] > m[maxIndex]){
            maxIndex = p;
         }
         p += 1;
      }
      return m[maxIndex];
   }
   public static void main(String[] args) {
      int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
      System.out.println(max(numbers));
   }
}
