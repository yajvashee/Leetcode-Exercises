# 191. Number of 1 Bits

## Problem
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?

## Approach
1. First find out how many bits are needed for this number.
2. To do that, we first start with the number 1 and keep doubling it until it is greater than the number.
3. By usng this approach we have not only foiund number of bits but also the last power of 2 that is less than the number.
4. We can then loop until that value is 1 or greater.
5. Check if the number is greater than start
6. If it is, then we increment count_bits by 1, subtract start from n.
7. We then keep halving start value so that it eventaully becomes less than 1 and the loop can end.
8. Once the loop has finished we return count_bits.