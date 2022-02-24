# """ Arrays """
# student = [0 for k in range(20)]
# print(student)
# student[0] = 25
# print(student)
#
# for k in range(len(student)):
#     student[k] = 7
# print(student)
#
# for k in range(len(student)):
#     if k % 2 == 0:
#         student[k] = "good"
#     else:
#         student[k] = k * k
#     print(f"student #{k} is {student[k]}")
#
# for item in student:
#     print(f"{item}", end = " ")
#     print(type(item))

# """Different Base Types"""
#
#
# class Employee:
#     """ Our second learning class """
#
#     def __init__(self):
#         # class-defined instance attribute (attributes)
#         self.name = None  # intended string
#         self.wage = None  # intended float
#         self.id = None  # intended int
#
#
# workers = [Employee for k in range(10)]
# print(Employee())
# print(Employee)
# workers = [Employee() for k in range(10)]
# #
# for k in range(len(workers)):
#     workers[k].name = "Employee #" + str(k)
#     workers[k].wage = 22.50
#     workers[k].id = 10000 + k
#     print(workers[k].name, workers[k].wage, workers[k].id)
# #
# for k in range(len(workers)):
#     worker = workers[k]
#     print(f"worker #{k} has name {worker.name}, "
#           f" id {worker.id} and earns {worker.wage}/hr.")


# student = [(2 * (6 + k ** 2)) for k in range(20)]
# for k in range(len(student)):
#     print(f"student #{k} is {student[k]}")
#
# student.append(290)
# print(student)
# print(len(student))

# array_size = 20
# student = [None for k in range(array_size)]
# print(student)

# intended constants referenceable from any function or main:
GREEN = 1
RED = 2
PURPLE = 3

# function definitions -----------------------------

# def abalone():
#     monster = int(input("give me an int to use for variable monster:"))
#
#     if monster == GREEN:
#         return 1.020203
#     elif monster == RED:
#         return some_num
#     elif monster == PURPLE:
#         return (1.020203 + some_num) / monster
#     else:
#         return 999
#
#
# some_num = 10
# print(abalone())

# # function definitions -----------------------------
#
# def my_func():
#     # assign a value to an expected local who_am_i and show
#     global who_am_i
#     who_am_i = 99
#     print(who_am_i)
#
#
# # main program -----------------------------------
# who_am_i = 1
# my_func()
#
# # does the assignment in my_func() affect main's who_am_i?
# print(who_am_i)

""" Local Behavior of Assignment Statements """
# def adder_plus(a, b):
#     b += int(input("how much extra should I add? "))
#     print(f"b = {b}")
#     return a + b
#
#
# one = 1
# two = 2
# ans = adder_plus(one, two)
# print(f"ans = {ans}")
#
#
#
# # function definitions -----------------------------
# def adder_plus(a, b):
#     """ adds the arguments plus extra chosen at run-time """
#     b += int(input("how much extra should I add? "))
#
#     print(f"b (inside function) = {b}")
#
#     return a + b
#
#
# # main program -----------------------------------
# """ another example of parameter passing """
#
# one = 9;
# two = 8
# print(f"two (before call) = {two}")
# ans = adder_plus(one, two)
# print(f"answer = {ans} , two (after call) = {two}")
#
# my_list = [1, 2, 3]
# # print(f"my_list is in {hex(id(my_list))}")
# # print(f"my_list[0] is in {hex(id(my_list[0]))}")
# my_list[0] = 999
# print(f"my_list is in {hex(id(my_list))}")
# print(f"my_list[0] is in {hex(id(my_list[0]))}")
# # print(f"1 is in id {hex(id(1))}")
# my_list.append(999)
# print(f"my_list[3] is in {hex(id(my_list[3]))}")
# print(f"999 is in id {hex(id(999))}")
# print(hex(id(my_list[0])))
# print(my_list[0])
# if my_list[0] is my_list[3]:
#     print("True")
# else:
#     print("False")
#
# my_list.extend(my_list)
# print(my_list)


sensors = {"4213": ("STEM Center", 0),
           "4201": ("Foundation Lab", 1),
           "4204": ("CS Lab", 2),
           "4218": ("Workshop Room", 3),
           "4205": ("Tiled Room", 4),
           "Out": ("Outside", 5)
           }

sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]
filter_list = [sensors[i][1] for i in sensors]


def recursive_sort(list_to_sort, key=0):
    """
            create recursive_sort and pass param 'list_to_sort' and 'key',
            set 'key' to default value of 0
        """
    changed = True
    sorted_list = list_to_sort.copy()

    while changed:
        changed = False
        length = len(sorted_list)

        if length == 0:
            return sorted_list
        for i in range(0, length - 1):
            one_item = sorted_list[i][key]
            next_item = sorted_list[i + 1][key]
            if one_item > next_item:
                [sorted_list[i], sorted_list[i + 1]] = [sorted_list[i + 1], sorted_list[i]]
                changed = True

    ret_list = [sorted_list[0]] + recursive_sort(sorted_list[1:], key)
    # call back recursive_sort function itself and append to the list of first sorted tuple.
    # everytime we call back the function and passing sliced list, it will pass a smaller list to sort
    return ret_list


# rm_sen_dict = {key: value[1] for key, value in sensors.items()}

def print_filter(sensor_list, filter_list):
    print(filter_list)
    tag = "[ACTIVE]"
    new_dict = {item[0]: item[1] for item in sensor_list}
    # print(new_dict)
    for i in filter_list:
        for items in sensor_list:
            if items[2] not in filter_list:
                pass
            else:
                pass


# ddef change_filter(sensors, sensor_list, filter_list):
#     """ create change_filter function """
#     sensors = {item[0]: item[2] for item in sensor_list}
#     changed = True
#     while changed:
#         print_filter(sensor_list, filter_list)
#         changed = False
#
#         user_input = input("Type the sensor to toggle (e.g. 4201) or x to end ")
#         for key in sensors:
#             if user_input == 'x' or user_input == 'x'.upper():
#                 break
#             elif 4000 < int(user_input)< 4200:
#                 print("Invalid sensor")
#                 continue
#             elif key == user_input:
#                 filter_list.remove(sensors[key])
#                 continue
#             # elif user_input != key and sensors[key] not in filter_list and 4200 < int(user_input) < 4300:
#             #     filter_list.append(sensors[key])
#             #     filter_list.sort()
#             #     continue






# print(rm_sen_dict)

sorted_list = recursive_sort(sensor_list, 0)
change_filter(sensors, sorted_list, filter_list)
