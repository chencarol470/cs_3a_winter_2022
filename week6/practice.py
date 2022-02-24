# from collections import OrderedDict
#
# class_list = {1: "Carol Chen", 2: "Ryan Lawrence", 3: "Shawn Ron", 4: "David Robinson",
#                5: "Dale Wen", 6: "Lingo Czeng", 7: "Danpen Ronald", 8: "Georg Clues",
#                9: "Sam Chen", 10: "Ken Chen", 11: "Lam Chen", 12: "Sue Chen"}
#
#
# class_list1 = {"one": "Carol Chen", "two": "Ryan Lawrence", "three": "Shawn Ron", "four": "David Robinson",
#                "five": "Dale Wen", "six": "Lingo Czeng", "seven": "Danpen Ronald", "eight": "Georg Clues",
#                "nine": "Sam Chen", "ten": "Ken Chen", "eleven": "Lam Chen", "twelve": "Sue Chen"}
#
# # find_student = (input("Who are you looking for? ")).title()
# #
# # found = False
# # for key in class_list:
# #     if find_student in class_list[key]:
# #         print(f"{class_list[key]} is in the list, the number is {key}")
# #         found = True
# #         break
#
# for key in class_list1.items():
#     print(key)
# """
# Traceback (most recent call last):
#   File "/Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week6/practice.py", line 5, in <module>
#     print(class_list[0])
# KeyError: 0
# """

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = []
# for key in pokemon:
#     print(key,pokemon[key])

# p_names.append(pokemon.items())
# print(p_names)

# item = pokemon.items()
# print(item)
# for item in pokemon.values():
#     print(item)
#
# for item in pokemon.keys():
#     print(item)
#
#
# #hash function
#
# search_key = "Seel"
# print("Key Found?", search_key in pokemon)
#
# for key in sorted(pokemon):
#     print(key)


# nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
#
# nums = nums[:4] + nums[5:]
# print(nums)

# numbers = [x for x in range(0,53)]
# print(numbers)
#
# numbers = range(0,53)
# print(numbers)

# import image
#
# img = image.image("/week6/lutherBellPic.jpeg")
#
# p = image.Pixel(45, 55)
# print(p.getRed(), p.getGreen(), p.getBlue())

# str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
#
# # Write your code here.
# for i in str_list:
#     length = 0
#     for j in i:
#         length += 1
#     print(length)str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
# #
# # # Write your code here.
# # for i in str_list:
# #     length = 0
# #     for j in i:
# #         length += 1
# #     print(length)

# addition_str = "2+5+10+20"
# str_list = addition_str.split("+")
# sum_val = 0
# for char in str_list:
#     num = int(char)
#     sum_val += num
# print(sum_val)

# x = " "
# print(len(x))

# str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
#
# output = "False, You aren't you?"
#
# if "false" in str1:
#     output
# elif "false" not in str1:
#     output = "True! You are you!"
# else:
#      output = "Neither true nor false!"
#
# print(output)

"""
For each string in the list words, find the number of characters in the string. 
If the number of characters in the string is greater than 3, 
add 1 to the variable num_words so that num_words should end up 
with the total number of words with more than 3 characters.
"""
# words = ["water", "chair", "pen", "basket", "hi", "car"]


# num_words = 0
#
# for word in words:
#     count = 0
#     for char in word:
#         count += 1
#     if count > 3:
#         num_words += 1
# print(num_words)

# """Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense.
# Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
# """
# words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
#
# past_tense = []
#
# for word in words:
#     for char in word[-1]:
#         if "e" not in char:
#             past_tense.append(word + "ed")
#         else:
#             past_tense.append(word + "d")
# print(past_tense)


"""
Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.

Score

Grade

>= 90   A

[80-90) B

[70-80) C

[60-70) D

< 60    F

The square and round brackets denote closed and open intervals. 
A closed interval includes the number, and open interval excludes it. 
So 79.99999 gets grade C , but 80 gets grade B.
"""
# scores = [77.51, 92.86, 98.01, 69.71, 78.52, 59.69, 60.49, 85.04, 87.33, 91.04]
#
# grade = []
#
# for score in scores:
#     if 100 >= score >= 90:
#         grades = "A"
#         grade.append(grades)
#     elif 80 <= score < 90:
#         grades = "B"
#         grade.append(grades)
#     elif 70 <= score < 80:
#         grades = "C"
#         grade.append(grades)
#     elif 60 <= score < 70:
#         grades = "D"
#         grade.append(grades)
#     elif score < 60:
#         grades = "F"
#         grade.append(grades)
#     else:
#         print("Invalid input")
# print(grade)

"""
A year is a leap year if it is divisible by 4; however, if the year can be evenly divided by 100, it is NOT a leap year, unless the year is also evenly divisible by 400 then it is a leap year. Write code that asks the user to input a year and output True if it’s a leap year, or False otherwise. Use if statements.

Year    Leap?

1944    True

2011    False

1986    False

1800    False

1900    False

2000    True

2056    True

Above are some examples of what the output should be for various inputs.
"""
# years = [1967, 1900, 1400, 1628, 1701, 1217, 1359, 1300, 2000, 1054,
# 1724, 1000, 1800, 1100, 2100, 1023, 1600, 1500, 1358, 1160,
# 1700, 1744, 2009, 1200, 1944, 2011, 2056, 1986, 1800, 1900]
#
# for year in years:
#     if year % 4 == 0:
#         if year % 400 == 0:
#             print(year,True)
#         elif year % 100 == 0:
#             print(year,False)
#         else:
#             print(year, True)
#     else:
#         print(year, False)

import copy
# y = "y"
# z = copy.deepcopy(y)
# print(z)

""" the standard of below unpacking and unpacking it into a list, b is a list"""
# a, c, *b = years
# print(a)
# print(c)
# print(b)


import math
# side1 = 3
# side2 = 4
#
# hypotenuse_len = ((side1 ** 2 + side2 ** 2) ** 0.5)
# hypotenuse_len_option_2 = math.sqrt(side1 ** 2 + side2 ** 2)

# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
#
# # Write your code here.
#
# same_letter_count = 0
#
# words = sentence.split()
#
# for word in words:
#     if word[0] == word[-1]:
#         same_letter_count += 1
# print(same_letter_count)

"""
Create one conditional so that if “Friendly” is in w, then “Friendly is here!” should be assigned to the variable wrd. If it’s not, check if “Friend” is in w. If so, the string “Friend is here!” should be assigned to the variable wrd, otherwise “No variation of friend is in here.” should be assigned to the variable wrd. (Also consider: does the order of your conditional statements matter for this problem? Why?)

2/9/2022, 10:48:30 PM - 11 of 11
1
w = "Friendship is a wonderful human experience!"
2
​
3
if "Friendly" in w:
4
    wrd = "Friendly is here!"
5
elif "Friendly" is not in w:
6
    wrd = "No variation of friend is in here."
7
​
8
print(wrd)
9
​
10
​
Result	Actual Value	Expected Value	Notes
Fail	'Frien...here!'	'Friend is here!'	Testing the value of wrd
Pass	'else'	'w = "...rd)\n\n'	Checking that you used an else clause.
Fail	'elif'	'w = "...rd)\n\n'	Checking that you used an elif clause.

"""
#
# w = "Friendship is a wonderful human experience!"
#
# if "Friendly" in w:
#     wrd = "Friendly is here!"
# elif "Friend" in w:
#     wrd = "Friend is here!"
# else:
#     wrd = "No variation of friend is in here."
#
# print(wrd)
#
# mylist = []
# mylist.append(5)
# mylist.append(27)
# mylist.append(3)
# mylist.append(12)
#
# # mylist = mylist[0:1] + [12] + mylist[2:]
# # print(mylist)
# mylist.insert(1, 12)
# print(mylist)
# print(mylist.index((3)))


# st = "Warmth"
# a = []
# a = a + [st]
# print(a)

# name = "Sally"
# greeting = "Nice to meet you"
# s = "Hello, {}. {}."
#
# print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.
#
# print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.
#
# print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.

# """
# A technical point: Since braces have special meaning in a format string,
# there must be a special rule if you want braces to actually be included in the final formatted string.
# The rule is to double the braces: {{ and }}. For example mathematical set notation uses braces.
# The initial and final doubled braces in the format string below generate literal braces in the formatted string:
# """
# a = 5
# b = 9
# setStr = 'The set is {{{}, {}}}.'.format(a, b)
# print(setStr)

# numbs = [5, 10, 15, 20, 25]
#
# for num in numbs:
#
#
#
# print(numbs)


