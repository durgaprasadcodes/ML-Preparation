import pandas as pd
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([0,-1,-2,-3,-4])

df = pd.DataFrame({"marks":arr1,"hours":arr2})

print(df)

correlation = df.corr()

print(correlation)