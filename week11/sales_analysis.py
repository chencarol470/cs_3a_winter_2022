import pandas as pd
import os
import matplotlib.pyplot as plt

pd.options.display.width = 0
pd.options.display.max_columns = None
pd.options.display.max_rows = None

ds = pd.read_csv("/Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week11/SalesAnalysis/Sales_April_2019.csv")
""" 
print(ds.head())
  Order ID                     Product Quantity Ordered Price Each      Order Date                      Purchase Address
0   176558        USB-C Charging Cable                2      11.95  04/19/19 08:46          917 1st St, Dallas, TX 75001
1      NaN                         NaN              NaN        NaN             NaN                                   NaN
2   176559  Bose SoundSport Headphones                1      99.99  04/07/19 22:30     682 Chestnut St, Boston, MA 02215
3   176560                Google Phone                1        600  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001
4   176560            Wired Headphones                1      11.99  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001
"""
path = "/Users/yingxiachen/PycharmProjects/cs_3a_winter_2022/week11/SalesAnalysis"
files = [file for file in os.listdir(path) if not file.startswith(".")]
all_months_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path + "/" + file)
    all_months_data = pd.concat(
        [all_months_data, current_data])  # don't forget to put all_month_data and current-data inside[]
all_months_data.to_csv("all_data.csv", index=False)
all_data = pd.read_csv("all_data.csv")
# print(all_data.head())

nan_df = all_data[all_data.isna().any(axis=1)]
# print(nan_df.head())
all_data = all_data.dropna(how="all")
# print(all_data.head())
nan_df = all_data[all_data.isna().any(axis=1)]
# print(nan_df)

""" Get rid of text in order date column """
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
# print(all_data)

""" make columns correct type """
all_data["Quantity Ordered"] = pd.to_numeric(all_data["Quantity Ordered"])
all_data["Price Each"] = pd.to_numeric(all_data['Price Each'])
all_data["Month"] = all_data['Order Date'].str[0:2]
all_data["Month"] = all_data["Month"].astype("int32")
# print(all_data.head())
all_data['Month 2'] = pd.to_datetime(all_data['Month'].astype('int32'))
# print(all_data.head())

def get_city(address):
    return address.split(",")[1].strip(" ")


def get_state(address):
    return address.split(",")[2].split(" ")[1]


all_data["City"] = all_data["Purchase Address"].apply(lambda x: f"{get_city(x)} ({get_state(x)})")
# print(all_data.head())

# """ Data Exploration """
#
# all_data["Sales"] = all_data['Quantity Ordered'].astype('int') * all_data['Price Each'].astype('float')
#
# print(all_data.groupby(["Month"]).sum())
#
# months = range(1,13)
# # print(months)
# plt.bar(months, all_data.groupby(["Month"]).sum()["Sales"])
# plt.xticks(months)
# plt.ylabel("Sales in USD ($)")
# plt.xlabel("Month number")
# print(plt.show())

""" Question: What city sold the most product? """
# keys = [city for city, df in all_data.groupby('City')]
#
# plt.bar(keys, all_data.groupby(['City']).sum()["Sales"])
# plt.ylabel("Sales in USD ($)")
# plt.xlabel("Month number")
# plt.xticks(keys, rotation='vertical', size=8)
# print(plt.show())


""" Question 3: What time should we display advertisements to maximize likelihood of customer's buying product? """
# # add hour column
# all_data['Hour'] = pd.to_datetime(all_data['Order Data'].dt.hour)
# all_data['Month number'] = pd.to_datetime(all_data['Order Date']).dt.minute
# all_data['Count'] = 1
# all_data.head()

# keys = [pair for pair, df in all_data.groupby(['Hour'])]
#
# plt.plot(keys, all_data.groupby(['Hour']).count()['Count'])
# plt.xticks(keys)
# plt.grid()
# plt.show()

# My reommendation is slighly before 11am or 7pm

""" Question 4: What products are most often sold together? """
# # https://stackoverflow.com/questions/43348194/pandas-select-rows-if-id-appear-several-time
df = all_data[all_data['Order ID'].duplicated(keep=False)]
# # # Referenced: https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df2 = df[['Order ID', 'Grouped']].drop_duplicates()

# Referenced: https://stackoverflow.com/questions/52195887/counting-unique-pairs-of-numbers-into-a-python-dictionary
from itertools import combinations
from collections import Counter

count = Counter()

for row in df2['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

for key,value in count.most_common(10):
    print(key, value)

