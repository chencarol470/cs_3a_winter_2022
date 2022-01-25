"""
    Assignment Two: Temperature Conversions
    Submitted by Ying Xia Chen
    Submitted: January 12, 2022

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.

    Assignment 1: Implement the print_header() that prints the opening
              lines for the STEM Center Project
"""

import sys


def print_header():
    """
    This function print a header for the STEM Center Project
    """
    print("STEM Center Temperature Project")
    print("Ying Xia Chen")


def convert_units(celsius_value, units):
    """ create conversion function called convert_units """
    if units == 0:      # condition check and see which units the celsius_value is
        return "That's " + celsius_value + " degrees Celsius"

    elif units == 1:  # if the unit is differed from celsius, do conversion below
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


def main():
    """
    Defines main function for print_header.
    """
    print_header()
    celsius_value = input("Please enter a temperature in degrees Celsius: ")
    units = int(input("Please enter the desired conversion "
                      "(0 for no conversion, 1 for Fahrenheit, 2 to kevin): ")
                )
    print(convert_units(celsius_value, units))


if __name__ == "__main__":
    """
    Is this module executed directly or is it imported into 
    another module, the code in main() is only executed when the module is imported.
    """
    main()


"""-------------------RUN ------------------------------
STEM Center Temperature Project
Ying Xia Chen
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 for Fahrenheit, 2 to kevin): 0
That's 45 degrees Celsius

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

Here is a fourth sample output:
STEM Center Temperature Project
Ying Xia Chen
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 for Fahrenheit, 2 to kevin): 3
*** Invalid Input, the conversion type must be 0,1, or 2): You entered an illegal value

---------------------END RUN ----------------------------"""
