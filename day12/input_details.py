import pandas as pd
no_of_records = int(input("Enter the number of records you want to enter: "))
data = []
for i in range(no_of_records):
    name = input(f"Enter name of employee {i + 1}: ")
    age = input(f"Enter age of employee {i + 1}: ")
    data.append({"name": name, "age": age, "Index": i + 1})

df = pd.DataFrame(data).set_index("Index")
csv_file = df.to_csv("input_file.csv")


 