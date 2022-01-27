# test = {}
# print(type(test))
# test["key1"] = "test"
# print(test)
#
# # or this: and this is string literal
# test1 = {"key":"test"}
# print(type(test1))
# print(test1)
#
# # set variable, looks like this is more commonly to be used in workspace.
# key = "key1"
# value = "value1"
# dict1 = {key:value}
# print(dict1)
#
# test2 = dict(key2 = "test2")
# print(test2)
#
# print(chr(2890))
# print(ord("h"))
# print(ord("a".upper()))
# # or
# print(ord(("a").upper()))
# # -----run--- 65
# print(ord("a"))
# #---run--- 97 (upper ASCII of A + 32 is the ASCII code for lower case a.
#
# print(ord("\\"))
# #--- run --- 92 is ASCII for \
# print(ord("3"))
# #--- run --- 51 is ASCII for 3
#
# my_str = "I attend Foothil College"
# my_sliced1 = "G" + my_str[1:] # I can actually use my_str again but the two my_str will have different location
#
# some_sub = my_str[:-16]
# print(some_sub)
# some_other_sub = my_str[-15:]
# print(some_other_sub)
#
# declaration = "My middle initial is Y, if you must know."
# new_str = f"id of declaration after {hex(id(declaration))}" # f string can be use anytime if you want to format a string
# print(new_str)
#
# list1 = []  # this is more legit to do it instead of using 1 = list()
# type(1)
#
# list_of_squares = [0, "zero", 1, "one", 4, "four",\
#                    16, "sixteen", 0.9999, "end"]
#
# print(list_of_squares)
# print(list_of_squares[1:5])
# list_of_squares.append(2)
# print(list_of_squares)
# list_of_squares.pop()  #pop without value of index and it's going to take out last value of the list
# print(list_of_squares)
# print(list_of_squares.reverse())
# print(list_of_squares.sort())

# test = hex(id(list_of_squares)) + ["new item"]
# print(test)

# my_set = {1,2,3,4,5}
# print(type(my_set))
# my_set.add(11)
# my_set.remove(4)  #remove 4 is remove the actual value of 4 from the set
# print(my_set)
# my_set = my_set.pop()
# print(my_set)

lst = [x for x in range(11) if x % 2 == 0]
print(lst)

celsius = [0, 10, 20.1, 34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print(fahrenheit)

lst1 = [ x ** 2 for x in [ x ** 2 for x in range(11)]]
print(lst1)