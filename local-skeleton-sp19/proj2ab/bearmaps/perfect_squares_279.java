package bearmaps;

import java.util.Arrays;

public class perfect_squares_279 {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for(int i = 1; i <=n; ++i){
            for (int j =1; j*j <=i; ++j){
                dp[i] = Math.min(dp[i], dp[i-j*j]+1);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        perfect_squares_279 test = new perfect_squares_279();
        System.out.println(test.numSquares(12));
    }
}
