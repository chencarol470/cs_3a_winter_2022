"""
    Assignment Eight: Dataset Class
    Submitted by Ying Xia Chen
    Submitted: February 24, 2022

    Assignment 8:
    Create a class to manage the temperature data

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


class TempDataset():
    """ create class used to represent TempDataset """

    # class ("static") attributes and intended constants
    ORIGINAL_DEFAULT_TEMP = 0
    ORIGINAL_DEFAULT_TUP = (0, 0, 0)

    MIN_LEN = 3
    MAX_LEN = 20

    # class attribute "num_of_temp" and it will change over time.
    num_of_temp = 0

    temp = ORIGINAL_DEFAULT_TEMP

    # initializer method --------------
    def __init__(self):
        self._data_set = None
        self._name = "Unnamed"

        # each time new TempDataset object is instantiated, the num_of_temp will be updated by 1
        TempDataset.num_of_temp += 1

    @classmethod
    def get_num_objects(cls):
        # classmethod for returning the num_of_temp from TempDataset
        return cls.num_of_temp

    # name getter method -----------
    @property
    def name(self):
        return self._name

    # name setter method -----------
    @name.setter
    def name(self, new_name):
        if TempDataset.MIN_LEN > len(new_name) or len(new_name) > TempDataset.MAX_LEN:
            raise ValueError
        else:
            self._name = new_name

    def process_file(self, filename):
        return False

    def get_summary_statistics(self, active_sensors=None):
        if self._data_set is None:
            return None
        return TempDataset.ORIGINAL_DEFAULT_TUP

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if self._data_set is None:
            return None
        return 0

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        if self._data_set is None:
            return None
        return 0


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

    # client side , Unit Test ------------------------------
    current_set = TempDataset()

    print("First test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 1:
        print("Success")
    else:
        print("Fail")

    second_set = TempDataset()

    print("Second test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 2:
        print("Success")
    else:
        print("Fail")

    print("Testing get_name and set_name: ")

    print("- Default Name:", end='')

    if current_set.name == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("- Try setting a name too short: ", end='')

    try:
        current_set.name = "to"
        print("Fail")
    except ValueError:
        print("Success")

    print("- Try setting a name too long: ", end='')

    try:
        current_set.name = "supercalifragilisticexpialidocious"
        print("Fail")
    except ValueError:
        print("Success")

    print("- Try setting a name just right (Goldilocks): ", end='')

    try:
        current_set.name = "New Name"
        if current_set.name == "New Name":
            print("Success")
        else:
            print("Fail")
    except ValueError:
        print("Fail")

    print("- Make sure we didn't touch the other object: ", end='')
    if second_set.name == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("Testing get_avg_temperature_day_time: ", end='')
    if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_num_temps: ", end='')
    if current_set.get_num_temps(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_loaded_temps: ", end='')
    if current_set.get_loaded_temps() is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_summary_statistics: ", end='')
    if current_set.get_summary_statistics(None) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing process_file: ", end='')
    if current_set.process_file(None) is False:
        print("Success")
    else:
        print("Fail")


if __name__ == "__main__":
    """ condition check and if if __name__ is equal to main """
    main()  # if the conditional check is true, then call the main function

""" -----------------------RUN CODE---------------------------------------------
/usr/local/bin/python3.9 /Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week8/AssignmentEight.py
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
First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name: 
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success

Process finished with exit code 0
-----------------------END--------------------------------------------------"""
