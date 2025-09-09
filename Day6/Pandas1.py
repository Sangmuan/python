import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\tuang.sangmuan\Day6\loan.csv")
print(data.head(5))

print(data.columns)
s = pd.Series([10,20,30,40], name="Numbers")
s