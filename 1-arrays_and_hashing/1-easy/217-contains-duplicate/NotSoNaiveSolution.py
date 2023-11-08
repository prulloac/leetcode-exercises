"""
Instantiate a set and loop through the array, adding each element to the set. If the element is already in the set, return true. If the loop finishes, return false.
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
