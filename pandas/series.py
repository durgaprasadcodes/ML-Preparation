import pandas as pd
import numpy as np

data = np.arange(1,6)

series = pd.Series(data,index=['a','b','c','d','e'])

print(series)
print(series>3.5)
print(series['a'])
print(series.loc['b'])
print(series[series%2==0])