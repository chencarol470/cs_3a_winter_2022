"""
    Assignment Three: Build Our Menu
    Submitted by Ying Xia Chen
    Submitted: January 12, 2022

    Assignment 3:
    Create a new file named lab_assignment 3.py.
    Copy your code from Lab Assignment 2 and paste it into you new file
    Add information to update the docstring to reflect Lab Assignment 3
    Add the new code you are writing to support the requirements for Lab Assignment 3
    Delete the main() the code used in lab_assignment 2 and write a new main() function to generate the required to be
    output (the Unit Test, for Lab Assignment 3

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.

    Assignment 1: This program demonstrates printing lines of text to the screen
"""
import sys


def print_header():
    """ create print_header function """
    print("STEM Center Temperature Project")
    print("Ying Xia Chen")


# noinspection PyUnreachableCode
def convert_units(celsius_value, units):
    """ create conversion function called convert_units """
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
    """
    Open a new file
    """
    print("New File Function Called")


def choose_units():
    """ create choose_units function """
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
        
What is your Choice? 1
New File Function Called

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? 2
Choose Units Function Called

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
Change Filter Function Called

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? 4
Summary Statics Function Called

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? 5
Print Temp by Day/Time Function Called

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? 6
Print Histogram Function Called

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? 9
Invalid Invoice

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? -1
Invalid Invoice

        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose Units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
        
What is your Choice? a
*** Please enter a number only ***

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

-----------------------------END RUN--------------------------------"""
