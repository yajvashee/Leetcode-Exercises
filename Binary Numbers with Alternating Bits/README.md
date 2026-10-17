# 693. Binary Numbers with Alternating Bits

## Problem
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 

Constraints:

1 <= n <= 231 - 1

## Approach
1. Convert the number to binary.
2. To do that find the number of bits.
3. So we start with 1, and we keep multiplying by 2 and check that the number is still greater than the number being multiploed by 2.
4. Once we find the number of bits, we can find the binary value.
5. We check if the number is greater than or equal to 2^(i).
6. If it is, we subtract 2^(i) from the value and move to the (i-1) power and so on.
7. Once we have the binary representation, we go through each character and check if the current and next character are the same.
8. If at any point they are the same, we return False.
9. If they are always different we return True.