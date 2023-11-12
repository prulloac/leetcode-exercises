import java.util.List;
import java.util.Arrays;
import java.util.HashSet;

/**
 * 
 * Given that set does not have duplicates, instantiate a set based on the array and check if length of the set is different from the length of the array.
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
class Solution {
    public boolean containsDuplicate(int[] nums){
        List<Integer> asList = Arrays.stream(nums).mapToObj(i -> Integer.valueOf(i)).toList();
        return new HashSet<>(asList).size() != asList.size();
    }
}
    

