sensors = {"4213": ("STEM Center", 0),
           "4201": ("Foundation Lab", 1),
           "4204": ("CS Lab", 2),
           "4218": ("Workshop Room", 3),
           "4205": ("Tiled Room", 4),
           "Out": ("Outside", 10)
           }

sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]

"""
Start with the code you created for Assignment Four. 
Add the function recursive_sort() which has as its parameters, list_to_sort (a list of tuples like the one you just made) and key. 
key should have a default value of zero, and refers to whether the list should be sorted by the first or second value in the tuple. 
Of course, recursive_sort() should call itself as part of the process.
The sorted part of the list will be growing from the end of the list (the greatest value). 
Each time you call recursive_sort, you should be calling with a smaller list. 
You can use slicing for this.

The output of your run should look exactly like those in the run below.  Notice that the original list remains in its original order.

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]

List sorted by room number
 [('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundations Lab', 1), ('Out', 'Outside', 5), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
"""


# for i in range(len(sensor_list)):
#     x = {*sensor_list[i]}
#     y = {*sensor_list[i]}
#     print(*sensor_list[i])
#     print(type(x))
#     # * with tuple list will cause the values to be unpacked


def recursive_sort(list_to_sort, key=0):
    # changed = True
    sorted_list = list_to_sort.copy()

    # while changed:
    length = len(sorted_list)
    changed = False
    # print("Before sorted")
    # print(sorted_list)
    if length == 0:
        return sorted_list
    for i in range(0, length - 1):
        # print("this is the sorted list at the beginning of for loop.")
        # print(sorted_list)
        one_item = sorted_list[i][key]
        next_item = sorted_list[i + 1][key]
        if one_item > next_item:
            [sorted_list[i], sorted_list[i + 1]] = [sorted_list[i + 1], list_to_sort[i]]
            # changed = True
    recursive_sort(sorted_list,key)
    # ret_list = [sorted_list[0]] + recursive_sort(sorted_list[1:], key)
    # # call back recursive_sort function itself to allow it to do the list_to_sort again
    # print(ret_list)
    return sorted_list


#

# option 2
# def recursive_sort(list_to_sort, key=0):
#     changed = True
#     sorted_list = list_to_sort.copy()
#     while changed:
#         changed = False
#         length = len(sorted_list)
#         for i in range(0, length - 1):
#             one_item = sorted_list[i][key]
#             next_item = sorted_list[i + 1][key]
#             # if one_item < next_item:
#             #     [sorted_list[i], sorted_list[i + 1]] = [sorted_list[i], sorted_list[i + 1]]
#             if one_item > next_item:
#                 [sorted_list[i], sorted_list[i + 1]] = [sorted_list[i + 1], sorted_list[i]]
#                 changed = True
#     return sorted_list

# def recursive_sort(list_to_sort,key = 0):
#     sorted_list = []
#     length = len(list_to_sort)
#
#     for i in range(length - 1):
#         if list_to_sort[i][key] > list_to_sort[i + 1][key]:
#             temp = list_to_sort[i]
#             list_to_sort[i] = list_to_sort[i + 1]
#             list_to_sort[i + 1] = temp
#     sorted_list.insert(0, temp)
#     recursive_sort(sorted_list, key)
#     return sorted_list

# option2
# def recursive_sort(list_to_sort, key = 0):
#
#     temp_list = list_to_sort.copy()
#     list_length = len(temp_list)
#     for i in range(list_length - 1):
#         if temp_list[i][key] > temp_list[i + 1][key]:
#             #wasp
#             temp = temp_list[i]
#             temp_list[i] = temp_list[i + 1]
#             temp_list[i + 1] = temp
#
#     if list_length - 1 > 1:
#         list_remain = temp_list[:-1]
#         temp_list = recursive_sort(list_remain, key) + [temp_list[list_length - 1]]
#
#     return temp_list

# print(recursive_sort(sensor_list))

def main():
    print("\nOriginal unsorted list\n", sensor_list)
    print("\nList sorted by room number\n", recursive_sort(sensor_list, 0))
    print("\nList sorted by room name\n", recursive_sort(sensor_list, 1))
    print("\nOriginal unsorted list\n", sensor_list)


if __name__ == "__main__":
    """ condition check and if if __name__ is equal to main """
    main()
