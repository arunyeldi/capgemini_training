import pandas as pd

data = {
    'Region': ['North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 200000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 344444, 91000,77000,88000]
}

df = pd.DataFrame(data)
df.set_index(['Region', 'State', 'Year'], inplace = True)
print(df)
# print(df.loc[('South', 'Tamil Nadu', 2021), 'Sales'])