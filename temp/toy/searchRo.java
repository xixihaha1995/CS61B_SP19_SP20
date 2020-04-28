public class searchRo {
    public static boolean search(int[] nums, int target) {
        if (nums.length==0) {
            return false;
        }
        if(nums.length ==1 && nums[0]==target){
            return true;
        }
        if(nums.length ==1 && nums[0] != target){
            return false;
        }
        //TODO Search for pivot
        int pivot = 0;
        for(int i=0;i<nums.length;i++){
            if(i==nums.length-1){
                break;
            }
            if(nums[i]>nums[i+1]){
                pivot = i+1;
                break;
            }

        }
        //TODO rearrange
        int[] newNums = new int[nums.length];
        System.arraycopy(nums,pivot,newNums,0,nums.length-pivot);
        System.arraycopy(nums,0,newNums,nums.length-pivot,pivot);
        //TODO binary search;
        int left  = 0;
        int right = nums.length-1;
        return internal(left,right,newNums,target);

    }
    private static boolean internal(int left, int right, int[] nums, int target) {
        int cur = (left + right)/2;
        if(cur==left ||cur==right){
            if(nums[left]==target){
                return true;
            }
            if(nums[right]==target){
                return true;
            }
            return false;
        }
        if (nums[cur] == target) {
            return true;
        } else {
            if(nums[cur] > target){
                return internal(left,cur,nums,target);
            }
            if(nums[cur] < target){
                return internal(cur,right,nums,target);
            }
            return false;
        }
    }
    private int circular(int pivot, int size){
        //TODO map should decrease the space size
        return 1;
    }
}
