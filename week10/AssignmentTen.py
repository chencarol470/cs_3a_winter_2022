"""
    Assignment Ten: Print Summary Statistics
    Submitted by Ying Xia Chen
    Submitted: March 11, 2022

    Assignment 10:
    Implementing Choose_Units Function / Printing Some Statistics.
"""
import math

sensors = {"4213": ("STEM Center", 0),
           "4201": ("Foundation Lab", 1),
           "4204": ("CS Lab", 2),
           "4218": ("Workshop Room", 3),
           "4205": ("Tiled Room", 4),
           "Out": ("Outside", 5)
           }

sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]
filter_list = [sensors[i][1] for i in sensors]
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K")
}
current_unit = 0


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
        self._data_set = []
        try:
            open_file = open(filename, "r")
        except FileNotFoundError:
            return False

        for next_line in open_file:
            data_tuple = tuple(next_line.split(','))
            for i in range(len(data_tuple) - 1):
                if data_tuple[i] == "TEMP":
                    try:
                        day = int(data_tuple[0])
                    except ValueError:
                        return False

                    try:
                        time = float(data_tuple[1])
                    except ValueError:
                        return False

                    hour_of_day = math.floor(time * 24)

                    try:
                        sensor = int(data_tuple[2])
                    except ValueError:
                        return False
                    try:
                        temp = float(data_tuple[4])
                    except ValueError:
                        return False
                    try:
                        self._data_set.append((day, hour_of_day, sensor, temp))
                    except ValueError:
                        return False

        open_file.close()

    def get_summary_statistics(self, active_sensors=None):
        if self._data_set is None or active_sensors is None:
            return None
        else:
            try:
                avg_temp = float(f'\
                            {self.get_avg_temperature_day_time(active_sensors, day=None, time=None):.2f}')
                min_temp = min(temp[3] for temp in self._data_set \
                               if (temp[2] in active_sensors))
                max_temp = max(temp[3] for temp in self._data_set \
                               if (temp[2] in active_sensors))
                temp_tup = (min_temp, max_temp, avg_temp)
                return temp_tup
            except TypeError:
                return None

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if self._data_set is None or len(active_sensors) == 0:
            return None
        else:
            sum_temp = 0
            count = 0
            for tup in self._data_set:
                if tup[2] in active_sensors:
                    if (tup[1] == time and tup[0] == day) or day is None or time is None:
                        count += 1
                        sum_temp += tup[3]
            ave_temp = sum_temp / count
            return ave_temp

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        if self._data_set is None:
            return None
        return len(self._data_set)

    @property
    def data_set(self):
        return self._data_set


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
        # return f"That's {celsius_value} degrees Celsius"
        return f" {celsius_value} C"
    elif units == 1:  # if the unit is differed from celsius, do conversion below,
        fahrenheit = float(celsius_value) * 9 / 5 + 32
        # return f'That\'s {"{:.2f}".format(fahrenheit)} degrees Fahrenheit'
        return f"{fahrenheit:.2f} F"
    elif units == 2:
        kevin = float(celsius_value) + 273.15
        # return f'That\'s {"{:.2f}".format(kevin)} degrees kevin'
        return f"{kevin:.2f} K"
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


def new_file(dataset):
    """ Open a new file """
    filename_input = input("Please enter the filename of the new dataset: ")
    dataset.process_file(filename_input)
    num_samples = dataset.get_loaded_temps()
    print(f"Loaded {num_samples} samples")
    while True:
        try:
            data_name_input = input("Please provide a 3 to 20 character name for the dataset my Data Set: ")
            dataset.name = data_name_input
            break
        except ValueError:
            print("Bad name input, it has to 3 to 20 character long.")
            continue


def choose_units():
    """ create choose units function """
    global current_unit
    while True:
        try:
            print(f"Current units in {UNITS[current_unit][0]}")
            print("Choose new units")
            for k, v in UNITS.items():
                print(f"{k} - {v[0]}")
            enter_unit = int(input("Which unit? "))
            if enter_unit not in UNITS:
                print("Please choose a unit from the list")
                continue
            else:
                current_unit = enter_unit
                convert_units(current_unit, enter_unit)
                break
        except ValueError:
            print("*** Please enter a number only ***")
            continue


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


def change_filter(sensor_list, active_sensors):
    """ create change_filter function to filter list with sensor_list """
    sensors = {item[0]: item[2] for item in sensor_list}
    while True:
        print_filter(sensor_list, active_sensors)
        user_input = str(input("Type the sensor to toggle (e.g. 4201) or x to end "))
        try:
            if user_input in sensors:
                for key in sensors:
                    if key == user_input or user_input.lower() == key:
                        filter_list.remove(sensors[key])
                        continue
            elif user_input == 'x' or user_input == 'x'.upper():
                break
            elif 4000 < int(user_input) < 4200:
                print("Invalid sensor")
                break
        except TypeError:
            print("Type Error")


def print_summary_statics(dataset, active_sensors):
    """ create print_summary_statics function """
    if dataset._data_set is None or active_sensors is None:
        print("Please load data file and make sure at least one sensor is active")
    else:
        try:
            summary_tup = dataset.get_summary_statistics(active_sensors)
            level_tup = ("Minimum", "Maximum", "Average")
            lvl_sum_dict = {level_tup[idx]: summary_tup[idx] for idx in range(len(summary_tup))}
            print(f"Summary statistics for Test Week")
            for k in lvl_sum_dict:
                print(f"{k} temperature: {convert_units(lvl_sum_dict[k],current_unit)}")

        except TypeError:
            print("Please load data file and make sure at least one sensor is active")


def print_temp_by_day_time(dataset, active_sensors):
    """ create print_temp_day_time function """
    print("Print Temp by Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    """ create print_histogram function """
    print("Print Histogram Function Called")


def main():
    """ create main function """
    print_header()
    sorted_list = recursive_sort(sensor_list, 0)

    # instantiate object of current_set for TempDataset()
    current_set = TempDataset()

    while True:
        try:
            print_menu()
            print(current_set.get_avg_temperature_day_time(filter_list, 5, 7))
            choice = int(input("What is your Choice? "))
            if choice == 1:
                new_file(current_set)
                continue
            elif choice == 2:
                choose_units()
                continue
            elif choice == 3:
                change_filter(sorted_list, filter_list)
                continue
            elif choice == 4:
                print_summary_statics(current_set, filter_list)
                continue
            elif choice == 5:
                print_temp_by_day_time(current_set, filter_list)
                continue
            elif choice == 6:
                print_histogram(current_set, filter_list)
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

""" ----------------------RUN CODE -----------------------------
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
            
None
What is your Choice? 4
Please load data file and make sure at least one sensor is active

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
None
What is your Choice? 1
Please enter the filename of the new dataset: Temperatures2022-03-07.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset my Data Set: aaa

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
20.45544117647059
What is your Choice? 4
Summary statistics for Test Week
Minimum temperature:  16.55 C
Maximum temperature:  28.42 C
Average temperature:  21.47 C

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
20.45544117647059
What is your Choice? 2
Current units in Celsius
Choose new units
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit? 1

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
20.45544117647059
What is your Choice? 4
Summary statistics for Test Week
Minimum temperature: 61.79 F
Maximum temperature: 83.16 F
Average temperature: 70.65 F

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
20.45544117647059
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
Type the sensor to toggle (e.g. 4201) or x to end 4204
4201: Foundation Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
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
            
19.910638297872342
What is your Choice? 4
Summary statistics for Test Week
Minimum temperature: 61.79 F
Maximum temperature: 83.16 F
Average temperature: 70.12 F

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
19.910638297872342
What is your Choice? 3
4201: Foundation Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end 4205
4201: Foundation Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end 4213
4201: Foundation Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end 4218
4201: Foundation Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end Out
4201: Foundation Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside
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
            
None
What is your Choice? 4
Please load data file and make sure at least one sensor is active

            Main Menu
            ---------
            1 - Process a new data file
            2 - Choose Units
            3 - Edit room filter
            4 - Show summary statistics
            5 - Show temperature by date and time
            6 - Show histogram of temperatures
            7 - Quit
            
None
What is your Choice? 7
Thank you for using the STEM center Temperature Project
------------------------------------END CODE ------------------------------------"""
