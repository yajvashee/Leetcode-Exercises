# 3114. Latest time you can obtain after replacing characters

## Problem
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.

 

Example 1:

Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:

Input: s = "0?:5?"

Output: "09:59"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".

 

Constraints:

s.length == 5
s[2] is equal to the character ":".
All characters except s[2] are digits or "?" characters.
The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.

## Approach
1. Convert s into a string so we can change the value when there is a ?.
2. For each character in s.
3. If it is the first character and there is a question mark.
4. Check the second value in the string. If second character is ? or less than 2, then change first character to 1. If the second character is greater than 1, then change the first character to 0.
5. If the second value of the string is ? and first character is 1, then change the second character to 1. If the second character is ? and the first character is 0, then change second character to 9.
6. Third character is always : so no change needed.
7. If 4th character is ? then change that to 5.
8. If 5th character is ?, then change that to 9. 