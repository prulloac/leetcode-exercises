# Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Example 1:

> Input: nums = [1,2,3,4]\
> Output: [24,12,8,6]

## Example 2:

> Input: nums = [-1,1,0,-3,3]\
> Output: [0,0,9,0,0]

## Constraints:

- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a `32-bit` integer.
 

# Source

https://leetcode.com/problems/product-of-array-except-self/

# Solutions

Loop through the array once using an index `i` and calculate the product of all elements to the left of `i` and store it in `answer[i]`. Then loop through the array again using an index `j` and calculate the product of all elements to the right of `j` and multiply it with `answer[j]` and store it in `answer[j]`.
