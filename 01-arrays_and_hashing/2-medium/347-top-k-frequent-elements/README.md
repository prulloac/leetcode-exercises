# Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.


## Example 1:

> Input: nums = [1,1,1,2,2,3], k = 2
>
> Output: [1,2]

## Example 2:

> Input: nums = [1], k = 1
>
> Output: [1]

## Constraints:

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

# Source

https://leetcode.com/problems/top-k-frequent-elements/

# Solutions

> Instantiate a hash table and loop through the array, adding each element to the hash table and incrementing its value by one. Then sort the hash table by the number of occurrences and return the first `k` elements.

- Time Complexity: `O(n log n)`
- Space Complexity: `O(n)`

## Fast-code Solution

<!-- if possible solution that might be a one-liner -->