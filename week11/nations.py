# series is the column
# index is the row

import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = 0
pd.options.display.max_columns = None
pd.options.display.max_rows = None

myDataFrame = pd.read_csv("https://psme.foothill.edu/~20033409@ad.fhda.edu/cs3a/nations.csv")

life_expect = range(1,100)
plt.bar(life_expect, myDataFrame["GDP (Billions)"])

# def get_population(population):
#     return population
#
#
# # print(myDataFrame.values)
# print(myDataFrame.head())  # get first five records out of the frame
#
# myDataFrame['population'] = myDataFrame["population"].apply(lambda x: f"{get_population(x)}")
# print(myDataFrame.head())

# print(myDataFrame.items)        # get all records from the frame, this work with options.display....
# print(myDataFrame.tail())   # get last five records out of the frame
# print(myDataFrame.head(6000))
# print(myDataFrame[["year","country","population"]])
# print(myDataFrame[["year", "country", "population"]].sort_values(["population","year"]))
# print(myDataFrame[0:6000])
# print(myDataFrame["population"].max())                          # show the max value of "population
# """ show the data of which country has max value of the column "population" (compare all the value in vertical list of
# 'population' and find out the max """
# print(myDataFrame.loc[myDataFrame["population"].idxmax()])
# print(myDataFrame.loc[myDataFrame["life_expect"].idxmax()])
# print(myDataFrame.loc[myDataFrame["life_expect"].idxmin()])
# print(myDataFrame.query("(region == 'East Asia & Pacific') and (year == 2014)")["life_expect"].mean())
# print(myDataFrame.query("(region == 'East Asia & Pacific') and (income == 'High income')")["life_expect"].mean() \
# > myDataFrame.query("(region == 'East Asia & Pacific') and (income == 'Low income')")["life_expect"].mean())

""" 
Notice in our data, there is a line for GDP per Capita but what if you want the raw GDP number?  
You can calculate that using a lambda function.  
We want the number in Billions of dollars (10^9 dollars) so it's easier to understand.  
Check to make sure everything looks ok too.
"""

# myDataFrame["GDP (Billions)"] = myDataFrame.apply(lambda  x: x['gdp_percap'] * x['population'] * 10 **-9, axis=1)
# print(myDataFrame.query("year == 2014")[["country","income", "population", "gdp_percap","GDP (Billions)"]])
# print(myDataFrame.sort_values(["country","income", "population", "gdp_percap","GDP (Billions)"]))
# nan_df = myDataFrame[myDataFrame.isna().any(axis=1)]
# print(nan_df.items)
# # df = myDataFrame.mean(axis=1)
# # print(df)
# myDataFrame = nan_df.dropna(how="all")
# print(myDataFrame.items)
