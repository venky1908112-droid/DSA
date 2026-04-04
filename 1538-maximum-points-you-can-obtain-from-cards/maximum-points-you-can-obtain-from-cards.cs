public class Solution {
    public int MaxScore(int[] nums, int k) {
        int left = 0;

        int right = nums.Length - k;
        int right_sum = 0;

        for(int i = right; i < nums.Length; i++) right_sum += nums[i];
        int left_sum = 0;
        int max_res = right_sum;
        while(left < k)
        {
            left_sum += nums[left];
            right_sum -= nums[right];
            left++;
            right++;
            max_res = Math.Max(max_res, left_sum + right_sum);
        }
        return max_res;
    }
}