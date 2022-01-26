import sys

while True:
    # intended constants in program - use UP_CASE style for these
    # three price points and the # trips per quarter
    LOW_PRG = 3.35
    MED_PRG = 3.75
    HIGH_PRG = 4.35

    # ask for user input
    mpg = float(input("How many miles per gallon does your car get, city "))
    distance = float(input("How many miles would you travel, round trip, to "
                           "come to the nearest college campus? "))

    if mpg < 0 or distance < 0:
        print("Input value errors")
        continue
    else:
        print(f"You get {mpg} MPG, city, and you drive {distance} miles to/from campus. \n")
        # Assume that a face-to-face section of some source meets on campus two nights a week over a 12 weeks section
        # establish the number of trips per quarter(not needed if we made
        # it final and gave it the value 12 * 2 above in the declaration
        trips_per_quarter = 12 * 2

        temp_var = trips_per_quarter * distance
        temp_var = temp_var / mpg
        lowest_cost = float(temp_var * LOW_PRG)
        med_cost = float(temp_var * MED_PRG)
        high_cost = float(temp_var * HIGH_PRG)
        high_cost_str = "{:.1f}".format(high_cost)
        print(f"At price of {LOW_PRG}, you can save {lowest_cost} per quarter, \n"
              f"At price of {MED_PRG}, you can save {med_cost} per quarter, \n"
              f"At price of {HIGH_PRG}, you can save {high_cost_str} per quarter. \n")

        # caculate the result for all 120 for one year
        result = float(lowest_cost * 120 * 3)
        print(f"At ${LOW_PRG} per gallon, the instructor's students will collectively save ${result} per year.\n")
        result = float(med_cost * 120 * 3)
        print(f"At ${MED_PRG} per gallon, the instructor's students will collectively save ${result} per year.\n")
        result = "{:.1f}".format(high_cost * 120 * 3)
        print(f"At ${HIGH_PRG} per gallon, the instructor's students will collectively save ${result} per year.\n")
        sys.exit()
