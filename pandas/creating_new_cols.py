import pandas as pd
dictionary = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "name": ["Alice", "Bob", "Charlie", "David", "Emma", "Anil", "Sunny", "Aura", "Alex"],
    "age": [22, 25, 21, 24, 23, 20, 24, 25, 22],
    "city": ["New York", "London", "Paris", "Tokyo", "Sydney", "Andhra Pradesh", "Telengaana", "Kerala" , "Kochi"]
}

data = pd.DataFrame(dictionary)

# Creating New Row

new_row = {"id":10,"name":"Arun","age":24,"city":"Eluru"}

data.loc[len(data)] = new_row

# print(data)

# Creating New Column

data["gender"] = ["M",'M','F','F','M','F','T','F','M','F']

print(data)