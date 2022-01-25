""" demonstration of the while loop """


# get the withdrawal amount from user
# def withdraw():
#     withdrawal = float(input("Amount of withdraw ($20 minimum): "))
#
#     # test and continue asking until user types a number >= 20:
#     while withdrawal < 20:
#         withdrawal = float(input("$20 Minimum. \nPlease try again: "))
#     else:
#         print("Withdraw done, please take the money from the machine.")
#
#
# withdraw()

# # test and continue asking until user types a number >= 20
# while (True):
#     withdrawal = float(input("Amount of withdrawal -- Must be >= $20: "))
#     if withdrawal >= 20:
#         break

# #constant secret value - obfuscate so the programmer doesn't even know it
# secret_value = int((25 * 9801 / 35 - 200) / (25 + 34 / 12))
# print("***", secret_value, " ***")
#
# # welcome message
# print("Try to guess the secret integer value ...")
#
# # now prepare to loop for the game, False gets us into the lop
# not_correct = True
#
# # test and continue asking until user types a number >= 20
# while not_correct:
#     guess = int(input("Your guess: "))
#     if guess == secret_value:
#         # they got it. wish them well and set loop control variable
#         print("Congratulations!!!")
#         not_correct = False # this will end the loop next time we test
#     elif guess < secret_value:
#         print("Too low. Guess higher")
#     else:
#         print("Too high. Guess lower")


# x = 0
# while x < 5:
#     print('x is currently: ',x)
#     print('x is still less than ' + str(5) + ', adding 1 to x')
#     x += 1
#     if x == 3:
#         print('x == 3')
#     else:
#         print('continuing..')
#         continue

# x = 0
#
# while x < 5:
#     print('x is currently: ' + str(x))
#     x += 1
#     if x == 2:
#         print('x == 2')
#         continue
#     else:
#         print(' x is still less than ' + str(5) + ', adding 1 to x')
#         # x += 1
# else:
#     print("All Done!")

# balance = 1000
# while balance > 0:
#     # lots of statements, then...
#     response = input("Enter a command (depends on application): ")
#
#     # if response is q or Q, user wants out
#     if (response == 'q' or response == 'Q'):
#         break
#
#     # otherwise continue with the loop.


# # DO NOT RUN THIS CODE!!!!
# while True:
#     print("I'm stuck in an infinite loop!")

# while True:
#     user_choice = int(input("Enter a number: "))
#     twice_number = user_choice * 2
#     print(f"Twice your number is {twice_number}")
#     if twice_number <= 100:
#         continue
#     else:
#         break

# while True:
#     try:
#         user_choice = int(input("Enter a number "))
#     except ValueError:
#         print("Hey, that's not a number!")
#         continue
#     twice_number = user_choice * 2
#     print(f"Twice your number is {twice_number}")
#     if twice_number <= 100:
#         continue
#     else:
#         break

NameError #Raised when a local or global name is not found. This applies only to unqualified names.
# The associated value is an error message that includes the name that could not be found.
TypeError
IndexError
ZeroDivisionError
SyntaxError
ArithmeticError
BufferError
AttributeError
LookupError
AssertionError
EOFError  # Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
# (N.B.: the io.IOBase.read() and io.IOBase.readline() methods return an empty string when they hit EOF.)
GeneratorExit
# Raised when a generator or coroutine is closed; see generator.close() and coroutine.close().
# It directly inherits from BaseException instead of Exception since it is technically not an error.
ImportError
#Raised when the import statement has troubles trying to load a module.
# Also raised when the “from list” in from ... import has a name that cannot be found.
ModuleNotFoundError
# A subclass of ImportError which is raised by import when a module could not be located. It is also raised
# when None is found in sys.modules.
# New in version 3.6.
KeyError
# Raised when a mapping (dictionary) key is not found in the set of existing keys.
KeyboardInterrupt
# Raised when the user hits the interrupt key (normally Control-C or Delete). During execution,
# a check for interrupts is made regularly. The exception inherits from BaseException
# so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.
MemoryError
# Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects).
# The associated value is a string indicating what kind of (internal) operation ran out of memory.
# Note that because of the underlying memory management architecture (C’s malloc() function),
# the interpreter may not always be able to completely recover from this situation;
# it nevertheless raises an exception so that a stack traceback can be printed,
# in case a run-away program was the cause.

NotImplementedError
OSError
#This exception is raised when a system function returns a system-related error,
# including I/O failures such as “file not found” or “disk full”
# (not for illegal argument types or other incidental errors).


# while True:
#     try:
#         user_choice = int(input("Enter a number "))
#     except ValueError:
#         print("Hey, that's anot a number!")
#         continue
#     else:
#         twice_number = user_choice * 2
#         print(f"Twice your number is {twice_number}")
#     finally:
#         # (ide in this block gets executed in every case, after the ecxcept: and after the else:
#         print("All done!")
#         break

# first_num = 1.23e7
# second_num = 1.23e-7
# third_num = 123456e11
# print(first_num, second_num, third_num)
#
# f_num = 191412.53321
# s_num = -666666666666.000000
# t_num = 1111.222223333344444555555666
# ft_num = 1111.222223333344444555556666677777
# print(f_num, s_num, t_num, ft_num)
# print(id(third_num))

age = 91
temp = age - 8
age = temp + 19
x_val = 35
print(age,temp,x_val)

