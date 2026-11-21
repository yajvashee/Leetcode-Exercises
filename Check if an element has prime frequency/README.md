# 3591. Check if an element has prime frequency

## Problem
You are given an integer array nums.

Return true if the frequency of any element of the array is prime, otherwise, return false.

The frequency of an element x is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

 

Example 1:

Input: nums = [1,2,3,4,5,4]

Output: true

Explanation:

4 has a frequency of two, which is a prime number.

Example 2:

Input: nums = [1,2,3,4,5]

Output: false

Explanation:

All elements have a frequency of one.

Example 3:

Input: nums = [2,2,2,4,4]

Output: true

Explanation:

Both 2 and 4 have a prime frequency.

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

## Approach
1. Create a dictioanry that has occurences for each element.
2. Go through each value of the dictioanry and then check if it is prime.
3. If one of the values is prime, return true.
4. If after going through the dictioanry there are no primes, return false.