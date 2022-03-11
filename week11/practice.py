import pandas as pd

kids_heights = pd.read_csv("http://psme.foothill.edu/~20033409@ad.fhda.edu/cs3a/kids-height-final.csv")
print(kids_heights)
print(type(kids_heights))
print(kids_heights["Age"])
print(type(kids_heights["Age"]))
print(kids_heights["Daniel"])
