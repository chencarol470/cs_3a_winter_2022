# week 2 (practice)
# ########## intended constants referenceable from any function or main:
# GREEN = 1
# RED = 2
# PURPLE = 3
#
#
# # function definitions -----------------
#
# def abalone():
#     monster = int(input("give me an int to use for variable monster: "))
#     # function statements, then ...
#
#     if monster == GREEN:
#         return 1.020203
#     elif monster == RED:
#         return some_num
#     elif monster == PURPLE:
#         return (1.20203 + some_num) / monster
#     else:
#         return 999
#
#
# # main program ----------------------
# some_num = 10  # referencable in any functions that come after this line
#
# def main():
#     some_abalone_thing = abalone()
#     some_other_thing = (1.5 + abalone()) + some_abalone_thing
#     yet_another_thing = (abalone() + 1) / (abalone() + 2)
#     print(abalone())
#
#     print(some_abalone_thing,some_other_thing,yet_another_thing)
#
#
# if __name__ == "__main__":
#     main()
#
#
# """ ------------------RUN---------------
#
# /usr/local/bin/python3.9 /Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/main.py
# give me an int to use for variable monster: 1
# give me an int to use for variable monster: 2
# give me an int to use for variable monster: 3
# give me an int to use for variable monster: 4
# give me an int to use for variable monster: 5
# 999
# 1.020203 12.520203 0.004729280719280719
#
# Process finished with exit code 0
#
# ----------------END RUN-------------------"""

# # function definitions ----------------
#
# def desk():
#     y = int(input("enter an integer ...: "))
#     return_val = x + y
#     return return_val
#
#
# def spaceControl():
#     return desk() / 5
#
#
# # the main program -------------------
#
# x = 10
#
#
# def main():
#     result = spaceControl()
#     print(result)
#
#
# if __name__ == "__main__":
#     main()

"""program that requests age and ends if negative"""

# # get user's age and convert to int
# import sys
#
# user_age = int(input("How old are you?"))
#
# # make sure they entered a non-negative number; end if not
# if user_age < 0:
#     print("Your age cannot be negative")
#       sys.exit()
#
# if (user_age >= 21):
#     print("Enjoy your beer.")
# else:
#     print("Sorry, I can't serve you.")
#
# # if we fall through here, they typed a positive or zero age - good.
# print(f"Got it. You're {user_age} years old.")
#
# """ test whether or not a user-enter integer is even or odd using modulo operation/% """

# # get user's age and store both as string and int
# user_age = (input("Please enter your age. "))
# user_age_int = int(user_age)
#
# if(user_age_int % 2 == 0):
#     print(f"{user_age_int} is even.")
# else:
#     print(f"{user_age} is odd.")

# Mutually Exclusive Evens: if/elif/else
import sys

from click import prompt

""" compte atmospheric pressure base on diving depth """

# user_str = input("What is your diving depth in feet? ")
# depth = int(user_str)
#
# if depth < 33:
#     print("Use 2 atm for your calculation.")
# elif depth < 66:
#     print("Use 3 atm for your calculation.")
# elif depth < 99:
#     print("Use 4 atm for your calculation")
# else:
#     print("You are down too deep!")


"""" Do not use below progressive indentation, but rather even indentation 
(AKA linear or stacked indentation) with elif statements like the previous one.  
# if (depth < 33):
#     print("Use 2 atm for your calculation.")
# else:
#     if (depth < 66):
#         print("Use 3 atm for your calculation.")
#     else:
#         if (depth < 99):
#             print("Use 4 atm for your calculation.")
#         else:
#             if (depth < 132):
#                 print("Use 5 atm for your calculation.")
#             else:
#                 print("You are down too deep!")
"""

# """ Some True Nesting Combined with Mutual Exclusivity
# """ If there is logic that is truly nested, then we would use progressive indentation.


# """ compute tax owed based on state and income """
# state = input("Does your state have income tax (y or n)? ")
#
# if (state == 'y'):
#     marriage_status = int(input("Do you single, married filing seperate or Married filing jointly? 1 for Single, "
#                                  "married filing seperate, 2 for Married filing jointly. "))
#     if marriage_status == 1:
#         income = int(input("What is your annual income? "))
#         if income < 9325:
#             tax_rate = .01
#         elif income < 22107:
#             tax_rate = .02
#         elif income < 34892:
#             tax_rate = .04
#         elif income < 48435:
#             tax_rate = .06
#         elif income < 61214:
#             tax_rate = .08
#         elif income < 312686:
#             tax_rate = .093
#         elif income < 375221:
#             tax_rate = .103
#         elif income < 625369:
#             tax_rate = 0.113
#         else:
#             tax_rate = .123
#     elif marriage_status == 2:
#         income = int(input("What is your annual income? "))
#         if income < 18650:
#             tax_rate = .01
#         elif income < 44214:
#             tax_rate = .02
#         elif income < 69784:
#             tax_rate = .04
#         elif income < 96870:
#             tax_rate = .06
#         elif income < 122428:
#             tax_rate = .08
#         elif income < 625372:
#             tax_rate = .093
#         elif income < 750442:
#             tax_rate = .103
#         elif income < 1250738:
#             tax_rate = 0.113
#         else:
#             tax_rate = 0.123
#     tax_owed = income * tax_rate
# else:
#     tax_owed = 0
#
# print(f"Tax owed is {tax_owed}")

# a = int(input("What is your number?"))
# b = int(input("What is your number?"))
#
# if a == b:
#     a -= 1
#     print(a)
# print(a)

# """
# Converting Between Numeric Data Type
# Compatibility and Conversion Between Two Numeric Types
# Implicit Numeric Widening or Narrowing
# """
# x = 3
# y = 1.9
# answer = x / y
# print("x / y =", answer)
#
# a = 30
# b = 60
# answer1 = (a + b) * (x / y)
# print("(a + b) * (x / y) = ", answer1)
#
# a = 30
# b = 60
# answer1 = (a + b) * (x / y)
# print("(a + b) * (x // y) = ", answer1)
#
# # this source
# answer2 = 17.5 + int(-5 / 3)
# print("17.5 + in(-5 / 3 =", answer2)
#
# # compare source
# answer2 = 17.5 + int(-5 // 3)
# print("17.5 + in(-5 // 3 =", answer2)
#
# print(int(-5 / 3))
# print((-5 // 3))

##
# user = "I am 34 years old"
# user_age = user[5:7]
# spouse_age = "36"
# age_difference = int(spouse_age) - int(user_age)
# print(age_difference)
#
# """
# Illegal and Legal Numeric string-to-Numeric Conversions
# The constructors int() and float() can do a lot.  For example, they'll happily ignore leading or trailing spaces:
# """

# total_sec = 7684
# hours = total_sec // 3600
# sec_still_remaining= total_sec % 3600
# minutes = sec_still_remaining // 60
# sec_finally_remaining = sec_still_remaining % 60
# print("Hour is",hours,"\n"
#       "remaining second is",sec_still_remaining, "\n"
#       "minutes is",minutes
#       )


# def check_time():
#     current_time = int(input("What time is it now? "))
#     waiting_time = int(input("Please enter the number of "
#                              "hours to wait for the alarm. "))
#     alarm_time = (current_time + waiting_time) % 24
#     print(alarm_time)
#
#
# check_time()

""""
It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. 
If you go on a wonderful holiday leaving on day number 3 (a Wednesday) 
and you return home after 10 nights you would return home on a Saturday (day 6).
Write a general version of the program which asks for the starting day number,
and the length of your stay, and it will tell you the number of day of the week 
you will return on.
"""


# def return_day():
#     date_of_leaving = int(input("Enter the day you are leaving at. "))
#     day_of_leaving = int(input(
#         "Enter the day you will be leave for vacation. "
#     ))
#     if date_of_leaving == 0:
#         week_of_leaving = (date_of_leaving + day_of_leaving) // 7
#         day_of_return = (date_of_leaving + day_of_leaving) % 7
#         print(f"You return home after {week_of_leaving} week, "
#               f"and return on day number {day_of_return}.")
#
#
# return_day()

# print("Hello World \t It's a sunny day!")
#
# my_sum = 1 + 2 + 3 + 4 + 5 \
#          + 6 + 7 + 8 + 9
# # \ eliminated the blank spaces between the numbers and operands and can not regconize the operation
# print(my_sum)
#
# print(id(5.323))
# print(id(5.))
# some_number = -10
# print(id(some_number))
# print(id(-10))
#
# str_welcome = print(prompt("Welcome to FootHill College"))
# str_question = input("What is your question?")
#
# print(str_question, end=' ')
#
# print(type(input))

# def check_MPG():
#     miles_driven = int(input("Enter the mile driven. "))
#     gallons_usage = int(input("Enter the number of gallons used. "))
#     mpg = miles_driven // gallons_usage
#     print(f"If you drove {miles_driven} miles and used {gallons_usage} "
#           f"gallons of gas, you would be averaging {mpg} miles per gallon.")


#
# y = "hi, " + "name"
# print("y =", y)

# FileIO
# try:
#     f = open('testfile.txt', 'r')
#     # f = open('testfile.txt', 'w')
#     f.write('Test write this')
#     f.close()
# except IOError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()

# try:
#     f = open('testfile_1', 'w')
#     f.write('Test write this')
#     a = 10/0
# except IOError:
#     print("Error: Could not find file or read data")
# except ZeroDivisionError:
#     print("You cannot divide by 0")
# except UnboundLocalError:
#     print("Error: UnBondLocalError occurred.")
# except:
#     """
#     any error will be caught up at except if we don't specify the error, like ZeroDivisionErro"""
#     print("An unexpected error occured.")
#
#
# else:
#     print("Content written successfully")
#     f.close()
# finally:
#     print("We are done")

# def askint():
#     while True:
#         try:
#             val = int(input("Please enter an integer: "))
#         except:
#             print("Looks like you did not enter an integer!")
#             continue
#         else:
#             print("Yep that's a integer!")
#             break
#         # finally:
#     print("Finally, code executed!")
# askint()

condition = True

while True:
    try:
        user_choice = int(input("Enter a number "))
    except ValueError:
        print("Hey, enter a number")
        continue
    twice_number = user_choice * 2
    print(f"Twice your number is {twice_number}")
    # break # Break out of the while loop when we successfully enter a number
    condition = False
    sys.exit()


number = 1.23e7 # 1.23 times 10 of 7
number = 1.23e-7 # 1.23 times 10 of minus 7

# we only have 64 bits for float
# decimal function




bob = turtle.Turtle()
for _ in range(6):
    bob.forward(50)
    bob.right(135)

paul = turtle.Turtle()
for _ in range(8):
    paul.forward(50)
    paul.left(135)
