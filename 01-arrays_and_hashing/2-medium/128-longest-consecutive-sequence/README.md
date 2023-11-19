# Problem

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Example 1:

> Input: nums = [100,4,200,1,3,2]\
> Output: 4\
> Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## Example 2:

> Input: nums = [0,3,7,2,5,8,4,6,0,1]\
> Output: 9

## Constraints:

- `0 <= nums.length <= 105`
- `109 <= nums[i] <= 109`

# Source

https://leetcode.com/problems/longest-consecutive-sequence/

# Solutions

Create a set of all numbers in the array. set the current maximum sequence length to 0. Loop through the array and for each number `n` check if `n-1` is in the set. If it is not, then `n` is the start of a sequence. Loop through the array again and for each number `m = n + 1` check if `m` is in the set. If it is not, then `n` is the end of a sequence, otherwise increment `m` and check again. Keep track of the current sequence given by `m - n` and update the maximum sequence length by comparing it with the current sequence length before incrementing `n`. Return the maximum sequence length
