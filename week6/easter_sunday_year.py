"""
RUNSTONE, CHAPTER 8.13

Implement the calculator for the date of Easter.

The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

Ask the user to enter a year. Compute the following:

a = year % 19

b = year % 4

c = year % 7

d = (19 * a + 24) % 30

e = (2 * b + 4 * c + 6 * d + 5) % 7

dateofeaster = 22 + d + e

Special note: The algorithm can give a date in April. You will know that the date is in April if the calculation gives you an answer greater than 31. (You’ll need to adjust) Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.

Your program should print an error message if the user provides a date that is out of range
"""

year = int(input("Enter the year you would like to check. "))

a = year % 19

b = year % 4

c = year % 7

d = (19 * a + 24) % 30

e = (2 * b + 4 * c + 6 * d + 5) % 7

dateofeaster = 22 + d + e

print(a, b, c, d, e, dateofeaster)
print(a, b, c, d, e, dateofeaster)
