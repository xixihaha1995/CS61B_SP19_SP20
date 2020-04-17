public class BreakContinue {
  public static void windowPosSum(int[] a, int n) {
    int l = a.length;
    for(int i = 0; i < l; i += 1){
      if(a[i] < 0){
        continue;
      }
      int sum = a[i];
      for(int j = 1; j <= 3; j += 1){
        if(i+j >= l){
          break;
        }
        sum += a[i+j];
      }
      a[i] = sum;
    }
  }

  public static void main(String[] args) {
    int[] a = {1, 2, -3, 4, 5, 4};
    int n = 3;
    windowPosSum(a, n);

    // Should print 4, 8, -3, 13, 9, 4
    System.out.println(java.util.Arrays.toString(a));
  }
}
