""" Assignment Four: Creating a Sensor Dictionary and List

Author: Mike Murphy
CWID: 20123456
Date: 10/17/2021

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
This function prints the standard header whenever the modulle is called.  """


def print_header():
    print("STEM Center Temperature Project")
    print("Mike Murphy\n")


def new_file(dataset):
    pass


def choose_units():
    pass


def change_filter(active_sensors):
    pass


def print_summary_statistics(dataset, active_sensors):
    pass


def print_temp_by_day_time(dataset, active_sensors):
    pass


def print_histogram(dataset, active_sensors):
    pass


def print_menu():
    print()
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")
    print()


def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    return celsius_value + 273.15


def main():
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }

    print_header()
    # Start of Unit Test code
    sensor_list = [(k, v[0], v[1]) for k, v in sensors.items()]
    filter_list = [v[1] for k, v in sensors.items()]
    print(sensor_list, filter_list)

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
    if sum(filter_list) == 15:
        print("Pass")
    else:
        print("Fail")
    # End of Unit Tets code

    while True:
        print_menu()
        try:
            choice = int(input("What is your choice? "))
            if choice == 1:
                new_file(None)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(None)
            elif choice == 4:
                print_summary_statistics(None, None)
            elif choice == 5:
                print_temp_by_day_time(None, None)
            elif choice == 6:
                print_histogram(None, None)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("*** Please enter a number only ***")


if __name__ == "__main__":
    main()
