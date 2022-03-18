"""
    Assignment Eleven: Pandas Table with Temperature Data
    Submitted by Ying Xia Chen
    Submitted: March 16, 2022

    Assignment 11:
    Use two dictionaries.
    Implement print_temp_by_day_time() to print a table that
    shows the average temperature in our labs by day of week and hour of day.
    We use the get_avg_temperature_day_time() function that we just implemented.
"""
import math
import pandas as pd
pd.options.display.width = 0
pd.options.display.max_columns = None
pd.options.display.max_rows = None

sensors = {"4213": ("STEM Center", 0),
           "4201": ("Foundation Lab", 1),
           "4204": ("CS Lab", 2),
           "4218": ("Workshop Room", 3),
           "4205": ("Tiled Room", 4),
           "Out": ("Outside", 5)
           }
DAYS = {
    0 : "SUN",
    1 : "MON",
    2 : "TUE",
    3 : "WED",
    4 : "THU",
    5 : "FRI",
    6 : "SAT"
}

HOURS = {
    0 : "Mid-1AM  ",
    1 : "1AM-2AM  ",
    2 : "2AM-3AM  ",
    3 : "3AM-4AM  ",
    4 : "4AM-5AM  ",
    5 : "5AM-6AM  ",
    6 : "6AM-7AM  ",
    7 : "7AM-8AM  ",
    8 : "8AM-9AM  ",
    9 : "9AM-10AM ",
    10 : "10AM-11AM",
    11 : "11AM-NOON",
    12 : "NOON-1PM ",
    13 : "1PM-2PM  ",
    14 : "2PM-3PM  ",
    15 : "3PM-4PM  ",
    16 : "4PM-5PM  ",
    17 : "5PM-6PM  ",
    18 : "6PM-7PM  ",
    19 : "7PM-8PM  ",
    20 : "8PM-9PM  ",
    21 : "9PM-10PM ",
    22 : "10PM-11PM",
    23 : "11PM-MID ",
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
        return f" {celsius_value:.2f}"
    elif units == 1:  # if the unit is differed from celsius, do conversion below,
        fahrenheit = float(celsius_value) * 9 / 5 + 32
        # return f'That\'s {"{:.2f}".format(fahrenheit)} degrees Fahrenheit'
        return f"{fahrenheit:.2f}"
    elif units == 2:
        kevin = float(celsius_value) + 273.15
        # return f'That\'s {"{:.2f}".format(kevin)} degrees kevin'
        return f"{kevin:.2f}"
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
                print(f"{k} temperature: {convert_units(lvl_sum_dict[k],current_unit)} {UNITS[current_unit][1]}")

        except TypeError:
            print("Please load data file and make sure at least one sensor is active")


def print_temp_by_day_time(dataset, active_sensors):
    """ create print_temp_day_time function """
    tmp = []
    column = [DAYS[k] for k in DAYS]
    idx = [HOURS[k] for k in HOURS]
    if dataset.get_loaded_temps() == 0:
        print("There is no temperature value loaded.")
    elif dataset._data_set is None or active_sensors is None:
        for i in range(0, 24):
            tmp.append((["---"] * 7))
        df = pd.DataFrame(tmp, columns=column)
        df.index = list(idx)
        print(df.head(30))
    else:
        for t in HOURS:
            tmp1 = []
            for d in DAYS:
                if t is None or d is None:
                    tmp1.append("---")
                else:
                    cnv_unit = convert_units(dataset.get_avg_temperature_day_time(active_sensors, day=d, time=t),\
                                             units=current_unit)
                    tmp1.append(cnv_unit)
            tmp.append(tmp1)
        df = pd.DataFrame(tmp, columns=column)
        df.index = list(idx)
        print(f"Average Temperatures for Test Week\n"
              f"Units are in {UNITS[current_unit][0]}")
        print(df.head(25))



        # for day in DAYS:
        #     if day == dataset._data_set[0]:
        #         tmp.append(dataset._data_set[3])
        #         print(tmp)
        #         # print(dataset.get_avg_temperature_day_time(active_sensors,day,time))



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
            # print(current_set.get_avg_temperature_day_time(filter_list, 5, 7))
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
            
What is your Choice? 5
           SUN  MON  TUE  WED  THU  FRI  SAT
Mid-1AM    ---  ---  ---  ---  ---  ---  ---
1AM-2AM    ---  ---  ---  ---  ---  ---  ---
2AM-3AM    ---  ---  ---  ---  ---  ---  ---
3AM-4AM    ---  ---  ---  ---  ---  ---  ---
4AM-5AM    ---  ---  ---  ---  ---  ---  ---
5AM-6AM    ---  ---  ---  ---  ---  ---  ---
6AM-7AM    ---  ---  ---  ---  ---  ---  ---
7AM-8AM    ---  ---  ---  ---  ---  ---  ---
8AM-9AM    ---  ---  ---  ---  ---  ---  ---
9AM-10AM   ---  ---  ---  ---  ---  ---  ---
10AM-11AM  ---  ---  ---  ---  ---  ---  ---
11AM-NOON  ---  ---  ---  ---  ---  ---  ---
NOON-1PM   ---  ---  ---  ---  ---  ---  ---
1PM-2PM    ---  ---  ---  ---  ---  ---  ---
2PM-3PM    ---  ---  ---  ---  ---  ---  ---
3PM-4PM    ---  ---  ---  ---  ---  ---  ---
4PM-5PM    ---  ---  ---  ---  ---  ---  ---
5PM-6PM    ---  ---  ---  ---  ---  ---  ---
6PM-7PM    ---  ---  ---  ---  ---  ---  ---
7PM-8PM    ---  ---  ---  ---  ---  ---  ---
8PM-9PM    ---  ---  ---  ---  ---  ---  ---
9PM-10PM   ---  ---  ---  ---  ---  ---  ---
10PM-11PM  ---  ---  ---  ---  ---  ---  ---
11PM-MID   ---  ---  ---  ---  ---  ---  ---

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
Please enter the filename of the new dataset: aaa
Loaded 0 samples
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
            
What is your Choice? 5
There is no temperature value loaded.

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
            
What is your Choice? 5
Average Temperatures for Test Week
Units are in Celsius
              SUN     MON     TUE     WED     THU     FRI     SAT
Mid-1AM     21.12   20.65   21.69   21.51   21.03   21.09   19.84
1AM-2AM     21.12   20.48   21.59   21.47   20.93   21.09   19.85
2AM-3AM     21.11   20.43   21.47   21.38   20.88   21.06   19.79
3AM-4AM     21.11   20.42   21.44   21.32   20.84   21.02   19.80
4AM-5AM     21.05   20.37   21.41   21.21   20.79   20.96   19.86
5AM-6AM     21.04   20.21   21.36   21.17   20.72   20.82   19.85
6AM-7AM     20.86   19.90   21.28   21.05   20.64   20.65   19.82
7AM-8AM     20.70   20.05   21.12   20.93   20.61   20.46   19.87
8AM-9AM     20.61   20.22   21.23   20.80   20.67   20.32   19.90
9AM-10AM    20.86   21.11   21.98   20.89   21.23   20.16   20.19
10AM-11AM   21.21   21.94   22.77   21.47   22.07   20.39   20.64
11AM-NOON   21.47   22.65   23.44   22.16   22.69   20.73   20.80
NOON-1PM    21.61   22.95   23.95   22.64   23.05   20.96   20.99
1PM-2PM     21.65   23.25   23.99   23.09   23.17   21.05   21.01
2PM-3PM     21.87   23.58   24.17   23.47   23.30   21.07   21.02
3PM-4PM     21.88   24.03   24.40   23.59   23.46   21.09   20.77
4PM-5PM     21.67   24.18   24.45   23.76   23.61   21.03   20.87
5PM-6PM     21.58   24.07   24.40   23.73   23.71   20.83   20.87
6PM-7PM     21.54   23.43   23.94   23.42   23.17   20.65   20.66
7PM-8PM     21.37   22.96   23.19   22.76   22.32   20.29   20.55
8PM-9PM     21.21   22.56   22.27   22.12   21.55   19.81   20.21
9PM-10PM    21.04   22.27   21.83   21.71   21.20   19.67   19.93
10PM-11PM   20.77   22.02   21.66   21.49   21.17   19.81   19.84
11PM-MID    20.79   21.90   21.59   21.25   21.14   19.84   19.73

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
            
What is your Choice? 5
Average Temperatures for Test Week
Units are in Fahrenheit
             SUN    MON    TUE    WED    THU    FRI    SAT
Mid-1AM    70.02  69.16  71.03  70.73  69.85  69.96  67.71
1AM-2AM    70.02  68.87  70.85  70.64  69.67  69.97  67.74
2AM-3AM    70.00  68.78  70.64  70.48  69.58  69.90  67.63
3AM-4AM    70.00  68.75  70.59  70.38  69.51  69.83  67.63
4AM-5AM    69.90  68.66  70.55  70.19  69.42  69.73  67.75
5AM-6AM    69.87  68.38  70.45  70.11  69.29  69.47  67.73
6AM-7AM    69.55  67.82  70.30  69.89  69.15  69.16  67.67
7AM-8AM    69.26  68.08  70.02  69.67  69.09  68.82  67.77
8AM-9AM    69.10  68.40  70.22  69.44  69.20  68.58  67.82
9AM-10AM   69.55  69.99  71.56  69.60  70.21  68.30  68.35
10AM-11AM  70.18  71.49  72.99  70.65  71.73  68.71  69.16
11AM-NOON  70.65  72.77  74.19  71.90  72.85  69.32  69.44
NOON-1PM   70.90  73.31  75.10  72.75  73.49  69.72  69.78
1PM-2PM    70.97  73.86  75.18  73.57  73.70  69.88  69.83
2PM-3PM    71.36  74.44  75.51  74.25  73.94  69.93  69.84
3PM-4PM    71.38  75.25  75.92  74.47  74.23  69.95  69.39
4PM-5PM    71.00  75.52  76.01  74.77  74.49  69.86  69.57
5PM-6PM    70.84  75.33  75.92  74.71  74.67  69.50  69.57
6PM-7PM    70.77  74.18  75.09  74.16  73.70  69.18  69.20
7PM-8PM    70.46  73.34  73.75  72.96  72.17  68.53  68.99
8PM-9PM    70.18  72.60  72.08  71.82  70.80  67.65  68.38
9PM-10PM   69.86  72.08  71.29  71.08  70.17  67.40  67.88
10PM-11PM  69.39  71.64  71.00  70.69  70.11  67.66  67.72
11PM-MID   69.43  71.41  70.87  70.24  70.05  67.72  67.52

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

------------------------------------END CODE ------------------------------------"""
