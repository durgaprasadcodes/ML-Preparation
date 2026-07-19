import pandas as pd

dataset = pd.read_csv(r"C:\Users\rolex\OneDrive\Desktop\ML Preparation\pandas\heart_disease_risk_2026.csv")

new_data = dataset.iloc[:10,:6] # 10 Rows & 5 Columns

print(new_data)

new_data.to_csv("created_csv_from_heart_disease_risk_dataset.csv",index=False)
