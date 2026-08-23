import pandas as pd

data = pd.read_csv(r"C:\Users\rolex\OneDrive\Desktop\ML Preparation\pandas\heart_disease_risk_2026.csv")

print(data)

new_data = data.iloc[:10,:5]

print(new_data)
print(new_data[["patient_id","age"]])
print(new_data[new_data["age"]>55])
print(new_data["age"]>55)

# Dataset Inspection ⭐⭐

print(new_data.head())
print(new_data.tail())
print(new_data.shape)
print(new_data.columns)
print(new_data.describe())
print(new_data.info())

# Value Counts ⭐⭐

print(new_data["sex"].value_counts())
print(new_data["age"].value_counts())

