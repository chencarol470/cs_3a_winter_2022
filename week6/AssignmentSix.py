"""
    Assignment Six: Bubble sort using recursion
    Submitted by Ying Xia Chen
    Submitted: January 20, 2022

    Assignment 6:
    Start with the code you created for Assignment Four.
    Change the Sensor Number for Outside to 5.
    Add the function recursive_sort() which has as its parameters, list_to_sort (a list of tuples like the one you just made) and key.
    key should have a default value of zero, and refers to whether the list should be sorted by the first or second value in the tuple.
    Of course, recursive_sort() should call itself as part of the process.
    The sorted part of the list will be growing from the end of the list (the greatest value).
    Each time you call recursive_sort, you should be calling with a smaller list.
    You can use slicing for this.
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


def change_filter():
    """ create change_filter function """
    print("Change Filter Function Called")


def print_summary_statics():
    """ create print_summary_statics function """
    print("Summary Statics Function Called")


def print_temp_by_day_time():
    """ create print_temp_day_time function """
    print("Print Temp by Day/Time Function Called")


def print_histogram():
    """ create print_histogram function """
    print("Print Histogram Function Called")


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


def main():
    """ create main function """
    print_header()
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
                change_filter()
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

    print("\nOriginal unsorted list\n", sensor_list)
    print("\nList sorted by room number\n", recursive_sort(sensor_list, 0))
    print("\nList sorted by room name\n", recursive_sort(sensor_list, 1))
    print("\nOriginal unsorted list\n", sensor_list)


if __name__ == "__main__":
    """ condition check and if if __name__ is equal to main """
    main()  # if the conditional check is true, then call the main function

"""------------------ RUN -----------------------
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
        
What is your Choice? 7
Thank you for using the STEM center Temperature Project

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundation Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 10)]

List sorted by room number
 [('4201', 'Foundation Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 10)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundation Lab', 1), ('Out', 'Outside', 10), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundation Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 10)]

Process finished with exit code 0
-------------------------------------------------------------"""

"""------- This is my output----------------

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundation Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 10)]

List sorted by room number
 [('4201', 'Foundation Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 10)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundation Lab', 1), ('Out', 'Outside', 10), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

# this is the output not matching the required output
Original unsorted list
 [('4204', 'CS Lab', 2), ('4201', 'Foundation Lab', 1), ('Out', 'Outside', 10), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

------------------------------------------"""
