from collections import defaultdict 
"""
Create a hashmap where each key is a sorted string and each value is an array of strings
that are anagrams of the key. Loop through the input array and for each string, sort it 
and check if it exists in the hashmap, if it does, add it to the array of strings that 
are anagrams of the key, otherwise create a new key with the sorted string and add the 
string to the array of strings that are anagrams of the key. Finally, loop through the 
hashmap and add each array of strings to the result array.
- Time complexity: O(n log n)
- Space complexity: O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charGroups = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            charGroups[sortedS].append(s)
        return list(charGroups.values())