"""
    Assignment Four: Creating a Sensor List and Filter List
    Submitted by Ying Xia Chen
    Submitted: January 20, 2022

    Assignment 4: Creating a Sensor Dictionary and List
    Populate sensors dictionary directly with sensor information
    Populate sensor_list and filter_list from sensors

    Assignment 3: Implementing a Menu
    Create a menu that the user will use to interact with our desired program.

    Assignment 2: Added convert_units(celsius_value, units):
    This function accepts a temperature in Celsius and
    if units = 0 returns the temperture in Celsius
    if units = 1 returns the temerature in Farenheit
    if units = 2 returns the temperature in Kelvin

    Assignment 1: Added print_header()
    This function prints the standard header whenever the modulle is called.
"""

import sys

sensors = {"4213": ("STEM Center", 0),
           "4201": ("Foundation Lab", 1),
           "4204": ("CS Lab", 2),
           "4218": ("Workshop Room", 3),
           "4205": ("Tiled Room", 4),
           "Out": ("Outside", 10)
           }

sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]
filter_list = [sensors[i][1] for i in sensors]

print("Testing sensors:")
if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 10:
    print("Pass")
else:
    print("Fail")

print("Testing sensor_list length:")
if len(sensor_list) == 6:
    print("Pass")
    print("Testing sensor_list content:")
    for item in sensor_list:
        if item[1] != sensors[item[0]][0]:
            print("Fail")
            break
    else:
        print("Pass")

print("Testing filter_list length:")
if len(filter_list) == 6:
    print("Pass")
else:
    print("Fail")

print("Testing filter_list content:")
if sum(filter_list) == 20:
    print("Pass")
else:
    print("Fail")


def print_header():
    """ create print header function  """
    print("STEM Center Temperature Project")
    print("Ying Xia Chen")


def convert_units(celsius_value, units):
    """ instantiate convert units function """
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


if __name__ == "__main__":
    """ condition check and if if __name__ is equal to main """
    main()  # if the conditional check is true, then call the main function

"""----------------------------------RUN-----------------------
Testing sensors:
Pass
Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing filter_list length:
Pass
Testing filter_list content:
Pass
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

Process finished with exit code 0

-----------------------------END RUN--------------------------------"""
