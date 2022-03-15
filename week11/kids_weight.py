import pandas as pd
pd.options.display.width = 0
pd.options.display.max_columns = None

""" Option 1 """
# age_height = pd.read_csv("kids-height-final.csv")
#
# print(age_height.head())
# print(age_height.values)

""" Option 2 """
ages_height = {'Daniel': [80, 109, 144, 179],
 'Anthony': [79, 114, 141, 172],
 'Jose': [86, 114, 141, 180],
 'Andrew': [87, 110, 149, 166],
 'Michael': [86, 105, 144, 172],
 'Jacob': [84, 113, 135, 168],
 'Alyssa': [83, 115, 126, 160],
 'Emily': [83, 114, 137, 161],
 'Ashley': [79, 105, 136, 167],
 'Samantha': [86, 109, 139, 158],
 'Jessica': [83, 103, 144, 164],
 'Jennifer': [85, 107, 132, 168]}
ah_frame = pd.DataFrame(ages_height)
print(ah_frame.head())