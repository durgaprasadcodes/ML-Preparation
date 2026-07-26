import pandas as pd
import numpy as np

data = {
    "id": [1,2,3,4,5,6,7,8,9,10],
    "name": ["Alice","Bob","Charlie","David","Emma",
             "Anil","Sunny","Aura","Alex","John"],
    "age": [22, np.nan, 21, 34, 23,
            20, np.nan, 25, 32, 28],
    "city": ["New York","London",np.nan,"Tokyo","Sydney",
             "Hyderabad","Hyderabad","Kochi",np.nan,"London"],
    "department": ["IT","HR","IT","Finance","IT",
                   "HR","Finance","IT","HR",np.nan],
    "salary": [50000,70000,np.nan,80000,55000,
               40000,75000,60000,np.nan,72000]
}

df = pd.DataFrame(data)

print(df.info())

print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].median())

df['city'] = df["city"].fillna(df["city"].mode()[0])

df['department'] = df["department"].fillna(df["department"].mode()[0])

df["salary"] = df["salary"].fillna(df["salary"].median())

print(df[(df["salary"]>60)])

print(df.groupby("department")["salary"].mean())

print(df.groupby("city")["name"].count())

print(df.groupby("department")["salary"].max())

print(df.groupby("city")["age"].mean().round())