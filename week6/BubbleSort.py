# list = [3, 1, 9, 2, 9]
#
# changed = True
#
# while changed:
#     print("New Loop!")
#     changed = False
#     for i in range(0, len(list) - 1):
#         print(list)
#         if list[i] > list[i + 1]:
#             (list[i + 1], list[i]) = (list[i], list[i + 1])
#             changed = True
import math

list1 = [5, 3, 2, 1, 4]


def sorted_list(list):
    return sorted(list)
    # for i in range(len(list) - 1):
    #     if list[i] > list[i + 1]:
    #         [list[i], list[i + 1]] = [list[i + 1], list[i]]
    #         print(list)


def main():
    print(sorted(list1))


if __name__ == "__main__":
    main()
