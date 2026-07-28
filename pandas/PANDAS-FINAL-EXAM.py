import pandas as pd

data = {
    "Name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Helen","Ivan","Jack"],
    "Age": [25,30,22,35,28,40,27,29,31,26],
    "Department": ["HR","IT","IT","Finance","HR","Finance","IT","HR","Finance","IT"],
    "Salary": [35000,60000,50000,80000,42000,90000,55000,41000,72000,52000],
    "Experience": [2,6,1,10,4,15,3,5,8,2],
    "City": ["Delhi","Mumbai","Hyderabad","Delhi","Chennai","Mumbai","Hyderabad","Delhi","Pune","Chennai"]
}

df = pd.DataFrame(data)

# =========== SECTION-A ==========

print(df.head())
print(df[-3:])
print(df.shape)
print(df["Department"].value_counts())
print(df.describe())
print(df[["Name","Salary"]])

# =========== SECTION-B ==========

print(df[df["Salary"]>50000]['Name'])
print(df[df["Department"]=='IT']["Name"])
print(df[(df["City"] == 'Delhi')&(df["Salary"]>40000)]["Name"])
print(df[(df["Age"]>25) & (df["Age"]<30)]["Name"])
print(df[~(df["Department"]=='Finance')]) 
print(df[df["Department"]!='Finance'])

# =========== SECTION-C ==========

print(df["Age"].sort_values(ascending=True))
print(df["Age"].sort_values(ascending=False))
print(df.sort_values(by=["Department", "Salary"]))

# =========== SECTION-D ==========

df["Bonus"] = df["Salary"]*.10
df["Total Salary"] =  df["Salary"] + df["Bonus"]
# df.rename(columns={"Department":"Dept"},inplace=True)
# print(df)

# =========== SECTION-E ==========
print(df.groupby("Department")["Salary"].mean())
print(df.groupby('Department')["Salary"].max())
print(df.groupby("Department")["Name"].count())
print(df.groupby("Department")["Experience"].mean())
print(
    df.groupby("Department")["Salary"].agg(
        ["mean","max","min","count"]
    )
)

# =========== SECTION-F ==========

df.loc[2, "Salary"] = None
df.loc[5, "Age"] = None

print(df.info())
print(df.isnull())
df['Salary'] = df['Salary'].fillna(df["Salary"].mean())
print(df[df["Experience"]>5]['Name'])
del df["Bonus"]
df.dropna(subset=["Age"],inplace=True)
print(df.isnull.sum())

# =========== SECTION-G ==========

print(df["Department"].unique())
print(df["City"].nunique())
print(df.nlargest(3,"Salary"))
print(df["Department"].isin(["IT","HR"]))