"""
Given that set does not have duplicates, instantiate a set based on the array and check if length of the set is different from the length of the array.
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    

