import pandas as pd
import numpy as np

# 1. Load the dataset and filter 'Manufacturer', 'Model', and 'Type' for every 20th row starting from 1st (row 0)
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df = df.iloc[::20, :][['Manufacturer', 'Model', 'Type']]
print("Filtered Cars Data (every 20th row):")
print(filtered_df)

# 2. Load the dataset again and replace missing values in 'Min.Price' and 'Max.Price' with their respective mean
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
print("\nUpdated Cars Data (Min.Price & Max.Price missing values replaced):")
print(df[['Manufacturer', 'Model', 'Min.Price', 'Max.Price']])

# 3. Generate a DataFrame with random integers and filter rows with row sum > 100
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
filtered_rows = df_random[df_random.sum(axis=1) > 100]
print("\nFiltered Random Data (Rows with row sum > 100):")
print(filtered_rows)