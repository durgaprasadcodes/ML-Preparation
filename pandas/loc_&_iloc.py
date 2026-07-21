import pandas as pd

dictionary = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "name": ["Alice", "Bob", "Charlie", "David", "Emma", "Anil", "Sunny", "Aura", "Alex"],
    "age": [22, 25, 21, 24, 23, 20, 24, 25, 22],
    "city": ["New York", "London", "Paris", "Tokyo", "Sydney", "Andhra Pradesh", "Telengaana", "Kerala" , "Kochi"]
}

data = pd.DataFrame(dictionary)


data["gender"] = ["F",'M','M','M','F','M','F','F','F']

# print(data.value_counts("gender"))

new_row1 = {"id":10,"name":"Alex","age":26,"city":"swedan"}
new_row2 = {"id":11,"name":"Aura","age":23,"city":"Italy"}

data.loc[len(data)] = new_row1
data.loc[len(data)] = new_row2

# print(data)

# print(data.iloc[1])

print(data.iloc[:5,:3])