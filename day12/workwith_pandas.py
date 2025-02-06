import pandas as pd
import numpy

data = {
    "Name": ['Arun', 'Anvesh', 'Ritvik'],
    'Age': [21, 22, 21],
    'City': ['NZB', 'HYD', 'HYD']
}

df = pd.read_csv('customers-1000.csv')

# print(df.head())  # first
# print(df.info())
# print(df.describe())
# print(df['Index'].mean())

# retrieving a row by name
# row_by_name = df[df['Index'] == 1]
# print(row_by_name)

# sorting by columns
# sort_order = df.sort_values(by = ['First Name', 'Index'], ascending=[False, True])
# print(sort_order)

print(df.to_json('customertojson.json', orient='records', indent=4))

# print(df.to_html('customertohtml.html', index=False))

print(df.to_csv('customertocsv.csv', index=False))

