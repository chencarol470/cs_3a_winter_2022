def split(my_str):
    return [char for char in my_str]

def reverse_str(my_str):
    my_list = split(my_str)
    print(my_list)
    for i in range(len(my_list) - 1):
        count = 0
        if my_list[i] == '0':
            count += 1
            print(count)
        if len(my_list) >= 3 and count >= 0 or len(my_list) < 3:
            switch_str = my_list[i]
            my_list[i] = my_list[len(my_list)-1]
            my_list[len(my_list)-1] = switch_str
            rev_str = ''.join(my_list)
            return rev_str
        else:
            return my_str

    # except SyntaxError:
    #     my_str = f"{my_str}"
    #     new_lst = split(my_str)
    #     switch_str = new_lst[i]
    #     new_lst[i] = new_lst[len(new_lst) - 1]
    #     new_lst[len(new_lst) - 1] = switch_str
    #     rev_str = ''.join(new_lst)
    #     return rev_str

# my_str1 = '123'!

print(reverse_str('123'))
print(reverse_str('1240023'))
print(reverse_str('12234233'))
# print(reverse_str(my_str1))