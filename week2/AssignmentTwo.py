"""
    Assignment Two: Temperature Conversions
    Submitted by Ying Xia Chen
    Submitted: January 12, 2022

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.

    Assignment 1: This program demonstrates printing lines of text to the screen
"""

import sys


def print_header():
    print("STEM Center Temperature Project")
    print("Ying Xia Chen")


# create conversion function called convert_units
def convert_units():

    celsius_value = input("Please enter a temperature in degrees Celsius: ")
    units = int(input("Please enter the desired conversion "
                      "(0 for no conversion, 1 for Fahrenheit, 2 to kevin): ")
                )

    # condition check and see which units the celsius_value is
    if units == 0:
        print("That's ", celsius_value, "degrees Celsius")

    # if the unit is differed from celsius, do conversion below,
    elif units == 1:
        fahrenheit = float(celsius_value) * 9 / 5 + 32
        print(f'That\'s {"{:.2f}".format(fahrenheit)} degrees Fahrenheit')

    elif units == 2:
        kevin = float(celsius_value) + 273.15
        print(f'That\'s {"{:.2f}".format(kevin)} degrees kevin')

    # if the input int is other number than 0,1,2,
    # print error message and exit the code(sys.exit()
    else:
        print(
            "***Invalid Input, the conversion type must be 0,1, or 2):"
            " You entered an illegal value"
            )
        sys.exit()


# create main function
def main():
    # calling the function print_header
    print_header()
    convert_units()


# condition check and if if __name__ is equal to main
if __name__ == "__main__":
    # if the conditional if check is true, then call the main function
    main()


"""-------------------RUN ------------------------------
STEM Center Temperature Project
Ying Xia Chen
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 for Fahrenheit, 2 to kevin): 0
That's  45 degrees Celsius

Here is a second sample output:
STEM Center Temperature Project
Ying Xia Chen
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 for Fahrenheit, 2 to kevin): 1
That's 113.00 degrees Fahrenheit

Here is a third sample output:
STEM Center Temperature Project
Ying Xia Chen
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 for Fahrenheit, 2 to kevin): 2
That's 318.15 degrees kevin

Here is a last sample output:
STEM Center Temperature Project
Ying Xia Chen
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 for Fahrenheit, 2 to kevin): 3
***Invalid Input, the conversion type must be 0,1, or 2): You entered an illegal value

---------------------END RUN ----------------------------"""