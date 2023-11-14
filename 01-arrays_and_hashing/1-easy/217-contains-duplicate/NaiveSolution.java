/**
 *
 * Check if any element in the array is duplicated by comparing each element with the rest of the array.
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j])
                    return true;
            }
        }
        return false;
    }
}