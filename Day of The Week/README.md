# 1185. Day of the Week

## Problem
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Note: January 1, 1971 was a Friday.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

## Approach
1. Create a list of the days of the week from Sunday to Saturday.
2. Calculate the difference in days between the date given and 1st January 1971.
3. Add the difference to the value 5(since 1st January 1971 was on a Friday and that is index 5 in the array) and do modulus division by 7(since 7 days in the week) to find the index.
4. Return the index in our list of days of the week and that will provide the day of the week we need.