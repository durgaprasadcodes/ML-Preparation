import pandas as pd

dictionary = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Anil", "Sunny", "Aura", "Alex", "John"
    ],
    "age": [22, 45, 21, 34, 23, 20, 34, 25, 32, 28],
    "city": [
        "New York", "London", "Paris", "Tokyo", "Sydney",
        "Hyderabad", "Hyderabad", "Kochi", "Kochi", "London"
    ],
    "department": [
        "IT", "HR", "IT", "Finance", "IT",
        "HR", "Finance", "IT", "HR", "Finance"
    ],
    "salary": [
        50000, 70000, 45000, 80000, 55000,
        40000, 75000, 60000, 65000, 72000
    ]
}

df = pd.DataFrame(dictionary)

# ============= FILTER ==============

print(df)

print(df[df["age"]>20])

print(df[df["salary"]>60000])

print(df[(df["age"]>25)&(df['city']=="London")])

print(df[(df["department"]=="IT")|(df["salary"]>50000)])

print(df[~(df["department"] == "HR")])

print(df[(df["age"]>25) & (df["age"]<35) & (df["salary"]>55000)]["name"])

# =========== GROUPBY ============

print(df.groupby("department")["salary"].mean().round(2))

print(df.groupby("city")["salary"].max())

print(df.groupby("department")["name"].count())

print(df.groupby("city")["salary"].sum())

print(df.groupby("department")["age"].mean().round())

print(df["salary"].sort_values(ascending=True))

