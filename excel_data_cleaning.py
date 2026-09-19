# Excel Sheet Cleaning using Pandas
# This script reads an Excel file, cleans the data, and saves a cleaned Excel/CSV file.

import pandas as pd

# Change this path to your Excel file location
excel_file = 'sample_data.xlsx'

# Read Excel file
try:
    df = pd.read_excel(excel_file)
    print("Excel file loaded successfully.")
except FileNotFoundError:
    print(f"File not found: {excel_file}")
    print("Please make sure the Excel file exists in the same folder.")
    exit()

# 1. Show original data
print("\nOriginal Data:")
print(df.head())

# 2. Remove extra spaces from all object columns
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str).str.strip()

# 3. Standardize text columns
if 'Name' in df.columns:
    df['Name'] = df['Name'].str.title()
if 'City' in df.columns:
    df['City'] = df['City'].str.lower()
if 'Email' in df.columns:
    df['Email'] = df['Email'].str.lower()

# 4. Convert numeric columns
for col in ['Age', 'Salary', 'Amount']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Fill missing values
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].replace('', 'Unknown')
    else:
        df[col] = df[col].fillna(0)

# 6. Remove duplicate rows
if {'Name', 'Email'}.issubset(df.columns):
    df = df.drop_duplicates(subset=['Name', 'Email'], keep='first')

# 7. Reset index
# df = df.reset_index(drop=True)

print("\nCleaned Data:")
print(df.head())

# Save cleaned data to a new Excel file
cleaned_file = 'cleaned_data.xlsx'
df.to_excel(cleaned_file, index=False)
print(f"\nCleaned Excel file saved as: {cleaned_file}")
