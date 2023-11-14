"""
Check if any element in the array is duplicated by comparing each element with the rest of the array.
Time complexity: O(n^2)
Space complexity: O(1)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for idx in range(len(nums)):
            for jdx in range(idx + 1, len(nums)):
                if nums[idx] == nums[jdx]:
                    return True
