# series is the column
# index is the row

import pandas as pd
pd.options.display.width = 0
pd.options.display.max_columns = None
pd.options.display.max_rows = None

myDataFrame = pd.read_csv("https://psme.foothill.edu/~20033409@ad.fhda.edu/cs3a/nations.csv")
# print(myDataFrame.values)
# print(myDataFrame.head())   # get first five records out of the frame
# print(myDataFrame.items)        # get all records from the frame, this work with options.display....
# print(myDataFrame.tail())   # get last five records out of the frame
# print(myDataFrame.head(6000))
# print(myDataFrame[["year","country","population"]])
# print(myDataFrame[["year", "country", "population"]].sort_values(["population","year"]))
# print(myDataFrame[0:6000])
# print(myDataFrame["population"].max())                          # show the max value of "population
""" show the data of which country has max value of the column "population" (compare all the value in vertical list of 
'population' and find out the max """
print(myDataFrame.loc[myDataFrame["population"].idxmax()])
