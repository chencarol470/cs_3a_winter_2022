"""
    Assignment Five: Reverse a List using Recursion
    Submitted by Ying Xia Chen
    Submitted: January 26, 2022

    Assignment 5: Use list comprehension to create a variable called "alphabet" that contained 26 alphabet letters.
                  Implement recursive function called reverse_a_list(my_list) and call itself with a smaller list until
                  the length of my_list is 1.

"""


def reverse_a_list(my_list):
    """ reverse a list """
    print(len(my_list))
    length = len(my_list)

    if length > 1:  # keep checking if the value of length is greater than 1
        ret_value = reverse_a_list(my_list[:length - 1])
        # if the condition is True,
        # we set a value to call back self function reverse_a_ list and allow it to run recursively with length - 1
        if ret_value is not None or ret_value != "":
            # Make sure ret_value is not None and empty string to return a reverse string without TypeError
            rev_list = my_list[length::-1]
            return rev_list
        return ret_value
    else:
        return


def main():
    """ main function, run all the code from here """
    alphabet = [chr(char) for char in range(97, 123)]
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()

"""-----------------------------RUN-----------------------------
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Process finished with exit code 0

---------------------------------------- END RUN -------------------------------------"""
