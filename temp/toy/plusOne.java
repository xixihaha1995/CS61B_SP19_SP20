public class plusOne {
    public static int[] plusOne(int[] digits) {
        int size = digits.length;
        for (int i = size-1; i>=0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i] += 1;
                return digits;
            }
        }
         int[] ret = new int[size + 1];
         ret[0] = 1;
         return ret;
//        if (digits[0] == 0) {
//            int[] ret = new int[size + 1];
//            ret[0] = 1;
//            return ret;
//        }



    }

    public static void main(String[] args) {
        int[] tes = new int[1];
        tes[0] = 9;
        System.out.println(plusOne(tes));
    }
}
