import java.util.HashSet;

/**
 *
 * Instantiate a set and loop through the array, adding each element to the set. If the element is already in the set, return true. If the loop finishes, return false.
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet set = new HashSet<>();
        for (int i : nums) {
            if (set.contains(i)) {
                return true;
            } else {
                set.add(i);
            }
        }
        return false;
    }
}