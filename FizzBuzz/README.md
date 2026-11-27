# 412. Fizz Buzz

## Problem
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104

## Approach
1. Create an empty list called output
2. Go through each number between 1 to n.
3. If number is divisible by 15, add "FizzBuzz" to output(This if condition needs to be done first). 
4. If number is divisible by 5, add "Buzz" to output.
5. If the number is divisible by 3, add "Fizz" to output.
6. ANything else add the number to the list.
7. Return the list output.