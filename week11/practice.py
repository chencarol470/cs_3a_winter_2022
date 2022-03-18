import numpy as np
import pandas as pd
from numpy.random import randn


pd.options.display.width = 0
pd.options.display.max_columns = None
# kids_heights = pd.read_csv("http://psme.foothill.edu/~20033409@ad.fhda.edu/cs3a/kids-height-final.csv")
# print(kids_heights)
# # ah_frame = pd.DataFrame(kids_heights) # this is same as line 7 through 8
# # print(ah_frame.head())
# # for column in kids_heights:
# #     print(column)
# # #
# print(kids_heights.iterrows())
# # # # print(kids_heights)
# print(type(kids_heights.columns))
# print(kids_heights.index)
# print(kids_heights.values)

# #
# # ttl = 0
# # count = 0
# # for idx in range(0, len(kids_heights.values)):
# #     print(kids_heights.values[idx][0])
# #     count += 1
# #     ttl += kids_heights.values[idx][1]
# # avg = ttl / count
# # print(avg)
#
# # print(type(kids_heights))
# # print(kids_heights["Age"])
# # print(type(kids_heights["Age"]))
# # print(kids_heights["Daniel"])
#
# """  Getting Data from Within Python   """
# ages_heights = [("Age","Daniel","Anthony","Jose","Andrew","Michael","Jacob","Alyssa","Emily","Ashley","Samantha","Jessica","Jennifer"),
# ("2yr",80,79,86,87,86,84,83,83,79,86,83,85),
# ("5yr",109,114,114,110,105,113,115,114,105,109,103,107),
# ("10yr",144,141,141,149,144,135,126,137,136,139,144,132),
# ("15yr",179,172,180,166,172,168,160,161,167,158,164,168)]
#
# print(type(ages_heights))
# print(type(ages_heights[1]))
# ah_frame = pd.DataFrame(ages_heights)
# print(ah_frame.head())
# # assign column names from first element of ages_height (a tuple of strings)
# ah_frame.columns = ages_heights[0]
# print(ah_frame.head())
# ah_frame.drop(ah_frame.index[0], inplace = True)
# print(ah_frame.head())
# ah_frame.set_index('Age', inplace = True)
# print(ah_frame.head())
# ad_frame = pd.DataFrame(ages_heights)
# print(type(ad_frame))
# print(type(ad_frame[0]), ad_frame[0])     # the column(vertical) value in the table list
# print(type(ad_frame[1]), ad_frame[1])
# print(type(ad_frame[0][0]), ad_frame[0][0]) #the row(horizontal) value of the table list
# print(type(ad_frame[0][1]), ad_frame[0][1]) #the row(horizontal) value of the table list
# print(type(ad_frame[1][1]), ad_frame[1][1])
# print(type(ad_frame[2][1]), ad_frame[2][1])
# print(type(ad_frame[1][0]), ad_frame[1][0]) # the column value read in vertical in the table list
# print(type(ad_frame[1][0]), ad_frame[1][1]) # the column value read in vertical in the table list

# sum = 0
# for lst in ad_frame.values:
#     for i in range(len(lst)-1):
#         if lst[0] == '2yr':
#             sum += lst[i + 1]
# print(sum)
# print(ad_frame.head())      # print the table of the ad_frame
# print(ad_frame.items)     #<bound method DataFrame.items of      0       1        2     3       4        5      6    \
#                             #   7      8       9         10       11        12
# print(ad_frame.keys())      # RangeIndex(start=0, stop=13, step=1)
# print(ad_frame.index)       #vertical key information) RangeIndex(start=0, stop=5, step=1)
# print(ad_frame.columns)     # RangeIndex(start=0, stop=13, step=1)
# print(ad_frame.iterrows)    # <bound method DataFrame.iterrows of
    # 0       1        2     3       4        5      6      7      8       9         10       11        12
# 0   Age  Daniel  Anthony  Jose  Andrew  Michael  Jacob  Alyssa  Emily  Ashley  Samantha  Jessica  Jennifer
# 1   2yr      80       79    86      87       86     84      83     83      79        86       83        85
# 2   5yr     109      114   114     110      105    113     115    114     105       109      103       107
# 3  10yr     144      141   141     149      144    135     126    137     136       139      144       132
# 4  15yr     179      172   180     166      172    168     160    161     167       158      164       168>

# sum = 0
# for idx in ad_frame.items():
#     print(idx)
    # if ad_frame[idx] == '2yr':
    #     sum += ad_frame[idx][0]
    #     print(sum)

#
# print(type(ad_frame[0][1]), ad_frame[0][1])
# print(ad_frame)
# print(ad_frame.head()) # above line is same as this line

# """ set 2multidimension table """
# data = [41, 12, 62]
# numpy_arr = np.array(data)
# labels = ["John", "Sally", "Tim"]
# my_series = pd.Series(numpy_arr,labels)
# my_series1 = pd.Series(labels)
# print(my_series)
# print(my_series1)
#
#
# # help(pd.Series())
# print(pd.Series(numpy_arr))
#
# ah_frame = pd.DataFrame(my_series)
# print(ah_frame.head())

# numpy_arr = np.array([data] * 3)
# print(numpy_arr)

# """ dict series """
# dict = {"John":42, "Sally":12, "Tim":62}
# my_series = pd.Series(dict)
# print(my_series.head())

# data = randn(5,3)
# dict1 = range(0,4)
# # print(data)
# my_series1 = pd.DataFrame(dict1,data)
# print(my_series1.head())

# lst = [[1,2], [4,5], [7,8]]
# idx = ['cobra', 'viper', 'sidewinder']
# col = ['max_speed', 'shield']
#
# df = pd.DataFrame(lst, index=idx, columns=col)
# print(df)
# viper_val = df.loc["viper"]
# print(viper_val)
# max_sp = df.loc["cobra", "max_speed"]  #getting the cobra row and max_speed index's value
# print(max_sp)

