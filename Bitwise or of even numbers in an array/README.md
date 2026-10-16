# 3688. Bitwise or of even numbers in an array

## Problem
You are given an integer array nums.

Return the bitwise OR of all even numbers in the array.

If there are no even numbers in nums, return 0.

 

Example 1:

Input: nums = [1,2,3,4,5,6]

Output: 6

Explanation:

The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

Example 2:

Input: nums = [7,9,11]

Output: 0

Explanation:

There are no even numbers, so the result is 0.

Example 3:

Input: nums = [1,8,16]

Output: 24

Explanation:

The even numbers are 8 and 16. Their bitwise OR equals 24.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

## Approach
1. Filter out all the even numbers from nums.
2. Set an initial value for num1 to 0(to do the first OR operation with a number in the list)
3. For each element in the list.
4. Call that element num2.
5. Perform or operation between num1 and num2 and store that result as num1.
6. Return num1 after each element has the OR operation applied to.