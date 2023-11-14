# Problem

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

## Example 1:

> Input: ["lint","code","love","you"]
>
> Output: ["lint","code","love","you"]
>
> Explanation:
>
> One possible encode method is: "lint:;code:;love:;you"

## Example 2:

> Input: ["we", "say", ":", "yes"]
>
> Output: ["we", "say", ":", "yes"]
>
> Explanation:
>
> One possible encode method is: "we:;say:;:::;yes"

## Constraints:

- The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
- Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

# Source

https://leetcode.com/problems/encode-and-decode-strings/

https://www.lintcode.com/problem/659/

# Solutions

