"""
Collection and Sequence Objects
Built-in Container Objects
Strings - Immutable, Iterable, A string is a collections of characters 0-9, a-z, A-Z, + - / ? spaces and many more
Lists - Mutable, Iterable e.g my_list = [4, 'Foothill College', ['a', 'list of strings']]
Tuples - Immutable, Iterable, similar to list but immutable. e.g my_tuple = (4, 'Foothill College', ['a', 'list of strings'])
A Sets - mutable, Iterable, the items in a set are unique: if you append an item to a set that is already in the set,
       it will not be added, the items in a set must be hashable, this is similar to the items being immutable.
       the contents of the set are sorted. e.g my_set = { 6, 2, 8, 7}, my_another_set = {[1, 3], [1, 2]}
Dictionaries - A dict organizes data values by association key:value pairs A dict object is mutable and an iterable.
                e.g my_dict = {}  # creates an empty dict object
                    my_dict["name"] = "Mike"
                    my_dict["occupation"] = 'Teacher'
Later in this course, you will learn how to create custom Classes that you can tailor to be Container Objects
"""

# my_string = "Happy Monday, Dude"
# my_string = my_string.upper()
#
# for l in my_string:
#     print(l)

# my_dict = {}
# my_set = {6,7,8,9}
# my_dict["name"] = "Carol"
# my_dict["occupation"] = "Softwear Engineering"
# print(my_dict)
# print(type(my_set))
# print(type(my_dict))
# my_set.add((6,6))
# print(my_set)
# my_dict["age"] = 30
# print(my_dict)
# print(my_dict["name"][0])


# String

# # string initializations
# hi_there_p = "Hello there. Python is "
# easy_phrase = "easy"
# hard_phrase = "not so easy"
# emphasis_punctuation = "!!"
# calm_punctuation = "."
#
# # output some combination of the strings already defined
# print(hi_there_p + easy_phrase + calm_punctuation)
# print(hi_there_p + hard_phrase + emphasis_punctuation)
#
# # and here's a bit of literal plus variable action
# print("Either way, I'm having fun" + emphasis_punctuation)
#
# hi_there_p = "Hello there. Python is "
# print (f"The two string lengths: {len(hi_there_p)} and {len('easy')}")
# Above, you see an example of the len() function being applied to both a literal, len('easy'),
# and a variable, len(hi_there_p). The important difference is that if there are quotes inside the parens,
# Python assumes this is a literal and measures its length directly.
# If there are no quotes,
# Python treats it like a variable and looks inside that variable's memory location
# for the string whose length it should measure.

# Notice that we used double quotes for the f-string and single quotes for the literal.
# Whenever you have quotes inside quotes you need to use different types of quotes to keep the interpreter from getting confused.


# How does Python send the length to your program? By replacing the entire expression len( ... whatever ...) by a number
# -- the integer number of characters in the string. In the above source,
# you see that we put the len() function calls (as they are referred to) inside a print() statement,
# so the numbers 23 and 4 are printed on the screen at run-time.

# Here's an example of an expression inside len()'s parens. Focus on the second line which has a concatenation operator inside the parens:
#
# hi_there_p = "Hello there. Python is "
# # length_of_entire_string = len(hi_there_p + "easy")
# # print (f"The complete string length is {length_of_entire_string}")
#
# print(ascii(hi_there_p))
# print(hi_there_p.isascii())
# print(ord("h"))
# print(ord("H"))
# print(chr(ord("Q")))
#
# print("Have a Wonderful Weekend!\t Senior ring \n Where legend never die.\\")

# my_string = "This is a wonderful world and MAC book alert to join the new world carpet on counter top."
# print(my_string[-4:-1])
#
# declaration = "My middle initial is W, if you must know."
# print(f"BEFORE: {declaration}")
# k = 21
# declaration = declaration[:k] + "G" + declaration[k + 1:]
# print(f"AFTER: {declaration}")
# declaration = f"{declaration[:k]}G{declaration[k + 1:]}"
# print(declaration)

# list_of_square = \
#     [0, "zero", 1, "one", 4, "four", \
#      9, "nine", 16, "sixteen", 0.999, "end"]
# print(list_of_square)
#
# answer = "No worry"
#
# print( "answer is "                   # continuation implied
#        + str(answer),                 # continuation implied
#        "There is more to this than"   # continuation implied and also ...
#        " you see here."               # ... string concatenation implied
#        )

# some_names = ["frank", "arnie", "yan", "crystal", "ying", "anand", "manuel", \
#               "misha", "mansoor", "tony", "felisha", "myrna", "fiona", "jack"]
# print(some_names[1],
#       some_names[5],
#       some_names[-1])
#
# # has the output:
# # arnie, anand jack

# # Sublists: Slicing Items in a list
# # Getting sublists from a larger master list is just like getting a substring of a string.
# # One uses the [ <start>: <end> ] notation,
# # remembering that <end> is one position past the desired end of the sublist:
#
# some_names = ["frank", "arnie", "yan", "crystal", "ying", \
#               "anand", "manuel", "misha", "mansoor", \
#               "tony", "felisha", "myrna", "fiona", "jack"]
#
# sublist_of_names = some_names[3:7]
# print(
#    "\noriginal names: " + str(some_names)
#    + "\n\nand the sublist is: " + str(sublist_of_names)
#    )
#
#
# # has the output:
# # original names: ['frank', 'arnie', 'yan', 'crystal', 'ying', 'anand', 'manuel', 'misha', 'mansoor', 'tony', 'felisha', 'myrna', 'fiona', 'jack']
# #
# # and the sublist is: ['crystal', 'ying', 'anand', 'manuel']


# # list Concatenation
# event_ints_to_8 = [0, 2, 3, 4, 6, 8, -2, -4, -6, -8]
# some_random_odds = [-5, 24687, 1, 15]
# my_list = event_ints_to_8 + some_random_odds
# print(my_list)

# Unpacking lists (and strings)
# We can place the items of a list into their own separate variables by a process with the chic name unpacking.
# You place the list on the RHS and all the comma-separated variables into which you want the elements to land on the LHS:

# peach_puff_list = [1., 0.855, 0.725]
#
# # unpack and display
# red, green, blue = peach_puff_list
# print(f"{peach_puff_list} contains the elements {red} {green} {blue}")
# print(green)
#
# """ ------------------------- RUN ----------------------------
#
# [1.0, 0.855, 0.725] contains the elements 1.0 0.855 0.725
#
# --------------------------------------------------------- """
#
# # The same can be done with strings,
# # although it's less useful since you would need lots of variables on the LHS for most strings:
#
# my_word = "DOG"
#
# # unpack and display
# red, green, blue = my_word
# print(f"{my_word} contains the elements {red} {green} {blue}")
#
# """ ------------------------- RUN ----------------------------
# DOG contains the elements D O G
# --------------------------------------------------------- """

# Fast Loading of lists
# We have a quick way to load a long list with same value.
# For example, if we wanted a list s1 having 50 items, each with value -1,
# and list s2 having 15 items, each with value "undefined", we use this syntax:

# # instantiate two lists, one of 50 ints, another of 15 strings
# s1 = [-1] * 50
# s2 = 15 * ["undefined"]
#
# # Without the * 50 and 15 * present,
# # we are merely setting up two lists of length 1 (each) containing the manual values presented.
# # What's new is the * operator.
# # Here, it means "do this 50 (or 15)" times.
# # This is how to initialize a long list all to the same value.
# # We could even put multiple items inside the brackets,
# # and those items would be repeated (cycled through) as many times as the * operator suggested. So:
#
# s1 = [-1, -2, "crypton"] * 10
# print(s1)

# pokemon = [[-1] * 5, [-2] * 5]
# print(type(pokemon))
# print(pokemon)

# # Mutability of lists
# # One difference between lists and strings is that lists can be changed: they are mutable.
# my_list = ["demon", "evil", "robber", "ghost", "zombie"]
# my_list[1] = "vampire"
# print(my_list)
# my_list.append("evil")
# print(my_list)
# my_list.append("nomeaning")
# print(my_list)
# del my_list[6]
# print(my_list)
# my_list.append("happy")
# print(my_list)
# my_list = []
# my_ano_list = [[]]
# my_3rd_list = [[[]]]
# print(len(my_list),len(my_ano_list),len(my_3rd_list))
#
# list = [[1, 2], [3, 4], [5, 6]]
# target_one = list[2][0]
# print("Our number is", target_one)

# inner_list_one = [0, 2, 4]
# outer_list_one = [-111, inner_list_one, -111]
# print(outer_list_one) # [-111, [0, 2, 4], -111]
# inner_list_one[1] = 5
# print(inner_list_one) # [0, 5, 4]
# print(outer_list_one) # [-111, [0, 5, 4], -111]
# print()

#
# inner_list_two = [0, 2, 4]
# outer_list_two = [-111, inner_list_two, -111]
# print(outer_list_two)  # [-111, [0, 2, 4], -111]
# inner_list_two = 5
# print(inner_list_two) # 5
# print(outer_list_two) # [-111, 5, -111] -> [-111, [0, 2, 4], -111]
# print()

"""
The for loop is good if you know, beforehand, how many times something will be repeated.  
If the number of times that something is to be repeated is determined based on user input or 
other factors known only at run time, then a while loop is preferred.
"""

# """
# The "Don't Care" Variable
# """
# print("The cat is hungry!")
# for count in range(10):
#     print("Meow")
#
# print("The cat is hungry!")
# for _ in range(10):
#     # The "DON'T CARE" Variable is " _ ",
#     # Note that there is no logical difference between using _ and count as the variable,
#     # but cool coders use _.
#     print("MEOW")
#
# my_list = []
# for i in range(21):
#     my_list.append(i)
# print(my_list)
#
# my_list = []
# for i in range(1,21):
#     my_list.append(i)
# print(my_list)
#
# """
# list comprehension
# """
# my_list = [i for i in range(1,21)]
# print(my_list)
#
# my_list = [i * i for i in range(1,21)]
# print(my_list)

# """
# Tuples
# """
#
# list_1 = [3, "three exactly", 2.1, "last"]
# print ("LIST 1 --------------\n"
#        "whole shebang: ", list_1,
#        "\nsecond element =", list_1[1])
#
# list_2 = [x ** 2 for x in range(3, 9)]
# print ("LIST 2 --------------\n"
#        "whole shebang: ", list_2,
#        "\nsecond element =", list_2[1])
#
# # mutability, nesting and slicing
# list_1[2] = "i'm new"
# list_2[3] = list_1[1:3]
# print ("\nmutating, nesting and slices --------------\n"
#         "list_1 =", list_1, "\nlist_2 =", list_2)
#
# print ("\nloops --------------")
# for item in list_2:
#    print(item,  "   ", end = '')

# """
# Unpacking
# """
# peach_puff_list = [1., 0.855, 0.725]
# red, green, blue = peach_puff_list
# print(peach_puff_list, "contains the elements", red, green, blue)

# """
# Summary
# Here's a program and output with all the code from above:
# """
#
# # manual list
# list_1 = [3, "three exactly", 2.1, "last"]
# print ("\nLIST 1 (manual) --------------\n"
#        "whole shebang: ", list_1,
#        "\nsecond element =", list_1[1])
#
# # list comprehension
# list_2 = [x ** 2 for x in range(3, 9)]
# print ("\nLIST 2 (comprehension) --------------\n"
#        "whole shebang: ", list_2,
#        "\nsecond element =", list_2[1])
#
# # mutability, nesting and slicing
# list_1[2] = "i'm new"
# list_2[3] = list_1[1:3]
# print ("\nmutating, nesting and slices --------------\n"
#        "list_1 =", list_1, "\nlist_2 =", list_2)
#
# # deleting and unpacking
# del list_1[3]
# a, b, c = list_1
# print ("\ndeletion and unpacking --------------\n"
#        "list_1 =", list_1,
#        "\n... and contains the elements <{}>, <{}>, and <{}>"
#        .format(a, b, c))
#
# # loops
# print ("\nloops --------------")
# for item in list_2:
#    print(item,  "   ", end = '')
#
# """ ------------------------- RUN ----------------------------
#
# LIST 1 (manual) --------------
# whole shebang:  [3, 'three exactly', 2.1, 'last']
# second element = three exactly
#
# LIST 2 (comprehension) --------------
# whole shebang:  [9, 16, 25, 36, 49, 64]
# second element = 16
#
# mutating, nesting and slices --------------
# list_1 = [3, 'three exactly', "i'm new", 'last']
# list_2 = [9, 16, 25, ['three exactly', "i'm new"], 49, 64]
#
# deletion and unpacking --------------
# list_1 = [3, 'three exactly', "i'm new"]
# ... and contains the elements <3>, <three exactly>, and <i'm new>
#
# loops --------------
# 9    16    25    ['three exactly', "i'm new"]    49    64
#
# --------------------------------------------------------- """

# """
# tuples are Similar to lists
# tuples, like lists, are a sequential compound data type, built from primitive or other class objects.
#
# Manual Instantiation and Multiple Type Capability
# At the most basic level, we can produce a tuple manually using the same syntax as lists, with one exception. Rather than brackets, [ ... ], we use parentheses, ( ... ):
#
# tup_1 = (3, "three exactly", 2.1, "last")
# Since there are four items in tup_1 we might call it a 4-tuple.
#
# In fact, tuples can be defined without the parentheses:
#
# tup_1 = 3, 2.1, "last"
#
# (That's a 3-tuple.) There's a special syntax for constructing tuples containing zero elements or one element:
#
# tup_nada = ()                              # must use empty parens
# tup_singleton = "dragon slayer",           # must have a trailing comma
#
# """
#
# """
# # manual tuple
# tup_1 = (3, "three exactly", 2.1, "last")
# print ("TUPLE 1 --------------\n"
#        "whole shebang: ", tup_1,
#        "\nsecond element =", tup_1[1])
# print("slice: ", tup_1[1:3])  # Slicing
#
# # unpacking
# a, b, c, d = tup_1  # Unpacking
# print ("\nunpacking --------------\n"
#        "tup_1 =", tup_1,
#        "\n... and contains the elements <{}>, <{}>, <{}> and <{}>"
#        .format(a, b, c, d) )
#
#
# """ ------------------------- RUN ----------------------------
#
# TUPLE 1 --------------
# whole shebang:  (3, 'three exactly', 2.1, 'last')
# second element = three exactly
# slice:  ('three exactly', 2.1)
#
# unpacking --------------
# tup_1 = (3, 'three exactly', 2.1, 'last')
# ... and contains the elements <3>, <three exactly>, and <2.1>
#
# --------------------------------------------------------- """
# """

# # tuple comprehension?
# list_2 = [x ** 2 for x in range(3, 9)]
# tup_2 = (x ** 2 for x in range(3, 9))
# print(list_2)
# print(tup_2, "We made it this far -- no error")
# print ("\nsecond element of wishful tuple =", tup_2[1])

# """
# /usr/local/bin/python3.9 /Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week4/Python_Container_Objects_Looping.py
# [9, 16, 25, 36, 49, 64]
# <generator object <genexpr> at 0x7fa6801a1900> We made it this far -- no error
#
# Process finished with exit code 0
# """
#
# """
# Huh? It's not a syntax error or run-time error, but it's not pretty and it's not what we want. What is being printed?
# Certainly not the tuple, but rather some sort of Python-ese that describes a user-unfriendly thing called a "generator."
#  And if we try to access an individual element of the purported tuple, we get a run-time error:
#
# print ("\nsecond element of wishful tuple =", tup_2[1])
#
# # """ ----------------------- RUN ---------------------
# #
# # Traceback (most recent call last):
# #   File "C:\Users\michael\PythonProjects\Working Project\Hello_World Experiment.py",
# #     line 45, in <module> print (  "\nsecond element of wishful tuple =", tup_2[1]  )
# # TypeError: 'generator' object is not subscriptable
# #
# # -------------------------------------------------- """
# # """

# Again, the word generator appears. Maybe this isn't a tuple after all. Let's compare the type of our first experiment,
# tuple_1 with the type of the generated pseudo tuple, tuple_2:

# # manual tuple
# tup_1 = (3, "three exactly", 2.1, "last")
# print("type of tup_1: ", type(tup_1))
# print()
#
# # tuple comprehension?
# tup_2 = (x ** 2 for x in range(3, 9))
# print("type of tup_2: ", type(tup_2))
#
#
# """ ------------------------- RUN ----------------------------
#
# type of tup_1:  <class 'tuple'>
#
# type of tup_2:  <class 'generator'>
#
# --------------------------------------------------------- """
# """
# Well, that settles it. We never actually instantiated a tuple using the comprehension. That produced only something called a generator. When placed in brackets, [ ... ] a comprehension turns a generator into a list, so we never realized that we were getting a magical conversion to list automatically:
#
# list_2 = [x ** 2 for x in range(3, 9) ]
# print ("\nLIST 2 (comprehension) --------------\n"
#        "whole shebang: ", list_2,
#        "\nsecond element =", list_2[1])
#
# However, this didn't work with tuples. To fix this, we convert the generator to a tuple manually using our familiar "type casting" syntax: int(), float(), str(), ... and now, tuple():
#
# """

#  # tuple comprehension - now it works
# tup_2 = tuple(x ** 2 for x in range(3, 9))  # add tuple() to turn the generator to tuple
# print("type of tup_2: ", type(tup_2))
# print ("\nTUPLE 2?\n"
#        "whole shebang: ", tup_2,
#        "\nsecond element =", tup_2[1] )

"""
Generators (Sneak Peek)
All of this is due to the fact that a generator expression is dynamic and not-persistant unless it is saved in 
some sequence data type (like list, string, tuple). This means that generators can produce values one-after-another, 
but they must be used immediately or stored -- or they are lost. This saves memory and
allows you to "generate" a series of values that is theoretically larger than the size of your computer memory 
as long as you use them (or lose them) one-by-one as they show up in the generator's for loop. 
It is also a faster operation than if it were saved in a list or tuple.
"""

# """
# tuples are Immutable
# A major difference between a list and a tuple is that a list is mutable while a tuple is not:
#
# list Mutation: No Problem
# Both direct assignment to a list element and deletion are forms of mutation supported by lists:
#
# list_1 = [3, "three exactly", 2.1, "last"]
# list_1[2] = "i'm new"
# del list_1[3]
# print ("\nmutating and deletion --------------\n"
#        "list_1 =", list_1)
#
# """
#
# """------------------------- RUN ----------------------------
#
# mutating and deletion --------------
# list_1 = [3, 'three exactly', "i'm new"]
#
# --------------------------------------------------------- """
# tuple Mutation: Not Possible.
# mutability, nesting and slicing
# tup_1[2] = "i'm new"            # error
# tup_2[3] = tup_1[1:3]           # error
#
#
# # will crash
# print ("\nmutating, nesting and slices --------------\n"
#        "tup_1 =", tup_1, "\nltup_2 =", tup_2)
# as you can see:
#
# Traceback (most recent call last):
#   File "C:\Users\michael\PythonProjects\Working Project\Hello_World Experiment.py",
#     line 43, in tup_1[2] = "i'm new"            # error
# TypeError: 'tuple' object does not support item assignment
# An attempt to use the del statement on tuples will also fail. (Try it.)
#
# The immutability of tuple objects is one of its reasons for existence. There are certain places in Python where an immutable type is required. We'll see one soon when we consider dictionaries. A list-like structure might be desirable for use in those places, but the list, being itself mutable, can't be used. A tuple satisfies the condition of being list-like while also fitting the requirement of certain non-mutable applications (like the keys for dictionaries).
# #
# #
# # """
#
# list_1 = [3, "three exactly", 2.1, "last"]
# list_1[2] = "i'm new"
# del list_1[3]
# print ("\nmutating and deletion --------------\n"
#        "list_1 =", list_1)
#
# tup_1 = (3, "three exactly", 2.1, "last")
# # # tup_1[2] = "i'm new"            # error
# # tup_2[3] = tup_1[1:3]           # error
# del tup_1[1]

"""
The immutability of tuple objects is one of its reasons for existence. 
There are certain places in Python where an immutable type is required. 
We'll see one soon when we consider dictionaries. 
A list-like structure might be desirable for use in those places, but the list, being itself mutable, can't be used. 
A tuple satisfies the condition of being list-like while also fitting the requirement of certain non-mutable 
applications (like the keys for dictionaries).
"""
#
# my_string = "I am not in USA"
#
# string_list = [my_string[i] for i in range(len(my_string))]
# print(string_list)
#
# print(hex(id(73)))

# my_string = "this"
# new_string = my_string
# print(hex(id(my_string)))
# print(hex(id(new_string)))
# my_string = "that"
# print(hex(id(my_string)))
# ano_string = "this"
# print(hex(id(ano_string)))
# print(hex(id(new_string)))

# my_list = [21, "This is so good", ["a", "list of string"], 99.99]
# del(my_list[0])
# print(my_list)
#
# new_list = [i ** i for i in range(20)]
# # for num in new_list:
# #     if num == 16777216:
# #         print("You hit the Jackpot")
#
# for i in range(len(new_list)):
#     if new_list[i] == 16777216:
#         print(i)
#         print("You hit the Jackpot")

# tup = {(2, 1), (9, 8)}
# for item in tup:
#     print(item[0])
# tup.add("this")
# print(tup)
# # tup.add([2,3])
# print(tup) # we have to add immutable object to the set of immutable objects(we have a set of tuples in this case(tup)
# # set only accept immutable values, see sample below
#
# # lists = {[3,2], [89,32]}
# # print(lists)
# # """
# # Traceback (most recent call last):
# #   File "/Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week4/Python_Container_Objects_Looping.py", line 602, in <module>
# #     lists = {[3,2], [89,32]}
# # TypeError: unhashable type: 'list'
# # """
# tup.add(5)
# print(tup)

string1 = "Now I'm ready \" to use the single quotes inside a string!"
print(string1)

"""
# """ """, this is called multiline string, and we call it docstring when we use it in first statement in the module or function 
"""
