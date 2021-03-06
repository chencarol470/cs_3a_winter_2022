"""
    Assignment Seven: Filter List
    Submitted by Ying Xia Chen
    Submitted: February 19, 2022

    Assignment 7:
    This module needs two lists (sensor_list, filter_list) and one dictionary (sensors).
    Ensure that the  recursive_sort() function is also included in this module.
    The recursive_sort() function definition should be at the top of the module with the other function definitions.
    The lists and dictionary should come just before the while loop that runs the menu in main().

"""
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


def print_header():
    """ create print_header function """
    print("STEM Center Temperature Project")
    print("Ying Xia Chen")


def convert_units(celsius_value, units):
    """ instantiate convert_units function """
    if units == 0:  # conditional check and see which units the celsius_value is
        return "That's " + celsius_value + " degrees Celsius"
    elif units == 1:  # if the unit is differed from celsius, do conversion below,
        fahrenheit = float(celsius_value) * 9 / 5 + 32
        return f'That\'s {"{:.2f}".format(fahrenheit)} degrees Fahrenheit'
    elif units == 2:
        kevin = float(celsius_value) + 273.15
        return f'That\'s {"{:.2f}".format(kevin)} degrees kevin'
    else:
        # if the input int is other number than 0,1,2,
        # print error message and exit the code(sys.exit())
        return "*** Invalid Input, the conversion type must be 0,1, or 2): You entered an illegal value"

    # noinspection PyUnreachableCode
    sys.exit()


def print_menu():
    """ create print_menu function """
    print(
        """
            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            """
    )


def new_file():
    """ Open a new file """
    print("New File Function Called")


def choose_units():
    """ create choose units function """
    print("Choose Units Function Called")


def print_filter(sensor_list, filter_list):
    """ create print_filter function to print """
    tag = "[ACTIVE]"
    for item in sensor_list:
        rm_num, rm_desc, sen_num = item
        act_sen = f"{rm_num}: {rm_desc} {tag}"
        if sen_num in filter_list:
            act_sen = act_sen
        else:
            act_sen = act_sen[:-9]
        print(act_sen)


def change_filter(sensors, sensor_list, filter_list):
    """ create change_filter function to filter list with sensor_list """
    sensors = {item[0]: item[2] for item in sensor_list}
    changed = True
    while changed:
        print_filter(sensor_list, filter_list)
        changed = False
        user_input = input("Type the sensor to toggle (e.g. 4201) or x to end ")
        for key in sensors:
            if user_input == 'x' or user_input == 'x'.upper():
                break
            elif 4000 < int(user_input) < 4200:
                print("Invalid sensor")
                continue
            elif key == user_input:
                filter_list.remove(sensors[key])
                continue
            # elif user_input != key and sensors[key] not in filter_list and 4200 < int(user_input) < 4300:
            # this is the elif check to append the removed list back.
            #     filter_list.append(sensors[key])
            #     filter_list.sort()
            #     continue

            changed = True


def print_summary_statics():
    """ create print_summary_statics function """
    print("Summary Statics Function Called")


def print_temp_by_day_time():
    """ create print_temp_day_time function """
    print("Print Temp by Day/Time Function Called")


def print_histogram():
    """ create print_histogram function """
    print("Print Histogram Function Called")


def main():
    """ create main function """
    print_header()
    sorted_list = recursive_sort(sensor_list, 0)
    while True:
        try:
            print_menu()
            choice = int(input("What is your Choice? "))
            if choice == 1:
                new_file()
                continue
            elif choice == 2:
                choose_units()
                continue
            elif choice == 3:
                change_filter(sensors, sorted_list, filter_list)
                continue
            elif choice == 4:
                print_summary_statics()
                continue
            elif choice == 5:
                print_temp_by_day_time()
                continue
            elif choice == 6:
                print_histogram()
                continue
            elif choice == 7:
                print("Thank you for using the STEM center Temperature Project")
                break
            else:
                print("Invalid Invoice")
                continue
        except ValueError:
            print("*** Please enter a number only ***")
            continue


if __name__ == "__main__":
    """ condition check and if if __name__ is equal to main """
    main()  # if the conditional check is true, then call the main function

""" -----------------------RUN CODE---------------------------------------------
/usr/local/bin/python3.9 /Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week7/AssignmentSeven.py
STEM Center Temperature Project
Ying Xia Chen

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
What is your Choice? 3
4201: Foundation Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end 4201
4201: Foundation Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end 4205
4201: Foundation Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end 4000
4201: Foundation Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end x

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
What is your Choice? 
-----------------------END--------------------------------------------------"""
