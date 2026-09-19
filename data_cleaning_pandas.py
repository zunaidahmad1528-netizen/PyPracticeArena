# Data Cleaning using Pandas
# This script reads a small dataset, cleans it, removes duplicates, and saves cleaned CSV.

import pandas as pd

# Sample raw data
raw_data = {
    'Name': ['  rahul ', 'Rahul', '  Neha ', 'Amit', 'Riya', 'riya '],
    'City': [' Delhi ', 'delhi', '', ' Mumbai ', 'Pune', 'pune'],
    'Age': ['25', '25', '30', '28', '22', '22'],
    'Salary': ['40000', '40000', '', '52000', '35000', '35000'],
    'Email': ['RAHUL@GMAIL.COM', 'rahul@gmail.com', ' NEHA@EXAMPLE.COM ', 'amit@gmail.com', 'riya@gmail.com', 'riya@gmail.com']
}

# Create DataFrame
df = pd.DataFrame(raw_data)

# 1. Remove extra spaces
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str).str.strip()

# 2. Standardize text columns
# Keep names in title case, city lower, email lower
if 'Name' in df.columns:
    df['Name'] = df['Name'].str.title()
if 'City' in df.columns:
    df['City'] = df['City'].str.lower()
if 'Email' in df.columns:
    df['Email'] = df['Email'].str.lower()

# 3. Convert numeric columns
if 'Age' in df.columns:
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
if 'Salary' in df.columns:
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# 4. Fill missing values
if 'City' in df.columns:
    df['City'] = df['City'].fillna('unknown').replace('', 'unknown')

# 5. Remove duplicates
# Based on Name and Email
if {'Name', 'Email'}.issubset(df.columns):
    df = df.drop_duplicates(subset=['Name', 'Email'], keep='first')

# 6. Reset index
# df = df.reset_index(drop=True)

print("Cleaned DataFrame:")
print(df)

# Save cleaned data to CSV
output_file = 'cleaned_data_pandas.csv'
df.to_csv(output_file, index=False)
print(f"\nCleaned data saved to {output_file}")
