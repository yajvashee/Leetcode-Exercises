# 119. Pascal triangle II

## Problem
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

## Approach
1. Create an empty array output for the output.
2. For every value betwwen 0 to rowIndex.
3. Calculate rowIndex! /(index! *(rowIndex - index)!) where x! = x * (x-1) * (x-2) * .... * 2 * 1.
4. Add the answer of that to output.
5. Return the arry output.