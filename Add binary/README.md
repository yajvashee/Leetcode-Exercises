# 67. Add Binary

## Problem
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

## Approach
1. Define number_a and number_b as 0. These variables will represent the decimal values of a and b respectively.
2. Convert both a and b to their decimal values using a for loop.
2a. For each character in a.
2b. Multiply that character by 2^i where i is the index of my for loop. Increment number_a by that amount.
3. Convert b to decimal value by using the same approach explained above as we did for a.
4. Compute the sum of a and b and store it as total.
5. Convert the denary value total to binary by using the bin function.
