"""
Instantiate a hash table and loop through the array, adding each element to the hash table and incrementing its value by one. Then sort the hash table by the number of occurrences and return the first `k` elements.
Time complexity: O(n log n)
Space complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Instantiate a hash table
        hash_table = {}
        # Loop through the array
        for num in nums:
            # Add each element to the hash table and increment its value by one
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        # Sort the hash table by the number of occurrences
        sorted_hash_table = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
        # Return the first `k` elements
        return [x[0] for x in sorted_hash_table[:k]]
