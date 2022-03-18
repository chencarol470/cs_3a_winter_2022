import pandas as pd

DAYS = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT"
}

HOURS = {
    0: "Mid-1AM  ",
    1: "1AM-2AM  ",
    2: "2AM-3AM  ",
    3: "3AM-4AM  ",
    4: "4AM-5AM  ",
    5: "5AM-6AM  ",
    6: "6AM-7AM  ",
    7: "7AM-8AM  ",
    8: "8AM-9AM  ",
    9: "9AM-10AM ",
    10: "10AM-11AM",
    11: "11AM-NOON",
    12: "NOON-1PM ",
    13: "1PM-2PM  ",
    14: "2PM-3PM  ",
    15: "3PM-4PM  ",
    16: "4PM-5PM  ",
    17: "5PM-6PM  ",
    18: "6PM-7PM  ",
    19: "7PM-8PM  ",
    20: "8PM-9PM  ",
    21: "9PM-10PM ",
    22: "10PM-11PM",
    23: "11PM-MID ",
}

# # day = pd.DataFrame([DAYS[k] for k in DAYS])
# time = pd.DataFrame([HOURS[k] for k in HOURS])
# # day.columns =[DAYS[k] for k in DAYS]
# print(day.head())
# print(time.head())

tmp = []
for i in range(0,24):
    tmp.append((["---"] * 7))

df = pd.DataFrame(tmp, columns=[DAYS[k] for k in DAYS])
df.index = list([HOURS[k] for k in HOURS])
print(DAYS[0])

