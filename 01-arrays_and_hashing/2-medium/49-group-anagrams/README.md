# Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

> An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Example 1:

> Input: strs = ["eat","tea","tan","ate","nat","bat"]
> 
> Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## Example 2:

> Input: strs = [""]
>
> Output: [[""]]

## Example 3:

> Input: strs = ["a"]
>
> Output: [["a"]]

## Constraints:

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

# Source

https://leetcode.com/problems/group-anagrams/

# Solutions

> Create a hashmap where each key is a sorted string and each value is an array of strings that are anagrams of the key. Loop through the input array and for each string, sort it and check if it exists in the hashmap, if it does, add it to the array of strings that are anagrams of the key, otherwise create a new key with the sorted string and add the string to the array of strings that are anagrams of the key. Finally, loop through the hashmap and add each array of strings to the result array.

> Hint: if possible by language, use a hashmap with default empty array as values, therefore an if statement might be omited and time performance will be improved.
- Time complexity: `O(n log n)`
- Space complexity: `O(n)`

