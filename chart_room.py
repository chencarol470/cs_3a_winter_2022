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
