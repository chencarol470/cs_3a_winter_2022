"""
Sensor Number	Room Number	Room Description
0	4213	STEM Center
1	4201	Foundations Lab
2	4204	CS Lab
3	4218	Workshop Room
4	4205	Tiled Room
5   Out	    Outside
"""

# Temperatures2017-08-06.csv

# Temperatures2022-03-07.csv

#  Temperatures2022-03-10.csv

if day is None and time is None:
    sum_temp += tup[3]

""" create print_summary_statics function """
if dataset._data_set is None or active_sensors is None:
    print("Please load data file and make sure at least one sensor is active")
else:
    try:
        summary_tup = dataset.get_summary_statistics(active_sensors)
        level_tup = ("Minimum", "Maximum", "Average")
        lvl_sum_dict = {level_tup[idx]: summary_tup[idx] for idx in range(len(summary_tup))}
        unit = UNITS[current_unit][1]
        if current_unit == 0:
            print(f"Summary statistics for Test Week")
            for k in lvl_sum_dict:
                print(f"{k} temperature: {lvl_sum_dict[k]} {unit}")

        if current_unit == 1:
            print(f"Summary statistics for Test Week")
            for k in lvl_sum_dict:
                val = float('{f:.2f}'.format(f=lvl_sum_dict[k] * 9 / 5 + 32))
                print(f"{k} temperature: {val} {unit}")

        if current_unit == 2:
            print(f"Summary statistics for Test Week")
            for k in lvl_sum_dict:
                val = float('{v:.2f}'.format(v=lvl_sum_dict[k] + 273.15))
                print(f"{k} temperature: {val} {unit}")

    # try:
    #     summary_tup = dataset.get_summary_statistics(active_sensors)
    #     level_tup = ("Minimum", "Maximum", "Average")
    #     unit = UNITS[current_unit][1]
    #     if current_unit == 0:
    #         print(f"Summary statistics for Test Week \n"
    #               f"{level_tup[0]} temperature: {summary_tup[0]} {unit} \n"
    #               f"{level_tup[1]} temperature: {summary_tup[1]} {unit} \n"
    #               f"{level_tup[2]} temperature: {summary_tup[2]} {unit} \n")
    #     if current_unit == 1:
    #         f_list = []
    #         for data in summary_tup:
    #             f_val = float('{f:.2f}'.format(f=data * 9 / 5 + 32))
    #             f_list.append(f_val)
    #         print(f"Summary statistics for Test Week \n"
    #               f"{level_tup[0]} temperature: {f_list[0]} {unit} \n"
    #               f"{level_tup[1]} temperature: {f_list[1]} {unit} \n"
    #               f"{level_tup[2]} temperature: {f_list[2]} {unit} \n")
    #     if current_unit == 2:
    #         k_list = []
    #         for data in summary_tup:
    #             k_val = float('{k:.2f}'.format(k=data + 273.15))
    #             k_list.append(k_val)
    #         print(f"Summary statistics for Test Week \n"
    #               f"{level_tup[0]} temperature: {k_list[0]} {unit} \n"
    #               f"{level_tup[1]} temperature: {k_list[1]} {unit} \n"
    #               f"{level_tup[2]} temperature: {k_list[2]} {unit} \n")
    #
    except TypeError:
        print("Please load data file and make sure at least one sensor is active")


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
        sum_temp = [temp[3] for temp in self._data_set \
                    if (temp[2] in active_sensors) and (temp[0] == day) and (temp[1] == time)]
        avg_temp = sum(sum_temp) / len(sum_temp)

        return avg_temp
