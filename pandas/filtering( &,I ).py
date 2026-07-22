import pandas as pd

dictionary = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "name": ["Alice", "Bob", "Charlie", "David", "Emma", "Anil", "Sunny", "Aura", "Alex"],
    "age": [22, 45, 21, 34, 23, 20, 34, 25, 32],
    "city": ["New York", "London", "Paris", "Tokyo", "Sydney", "Andhra Pradesh", "Telengaana", "Kerala" , "Kochi"]
}

data = pd.DataFrame(dictionary)

# print(data)

# ====== 1. Single Condition ========

# print(data[data["age"]>30])
# print()
# print(data[data["city"]=="Tokyo"])
# print()

# ====== 2. AND (&) ===== 

# print(  data[(data["age"]>30) & (data["age"]<40)]   )
# print()
# print(data[(data["age"]>=20) & (data["name"]=='Anil')])

# ===== 3. OR(|) ======

# print(data[(data["age"]>45)|data["age"]<45])
# print(data[(data["age"]>40)|(data["age"]>30)])

# ====== 4. NOT(~) =======
print(data[~(data["age"]>40)])

