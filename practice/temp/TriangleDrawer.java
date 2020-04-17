
public class TriangleDrawer {
   public static void drawTriangle(int N) {
      int lin = 1;
      while ( lin <= N){
         int col = 1;
         while (col <= lin){
            System.out.print('*');
            col += 1;
         }
         System.out.println();
         lin += 1;
      }
      
   }
   
   public static void main(String[] args) {
      int N = 10;
      drawTriangle(N);
      
   }
}
