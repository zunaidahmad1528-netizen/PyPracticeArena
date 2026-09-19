# Data Cleaning Example
# This script removes spaces, fixes case, removes duplicates, and saves cleaned data

# Raw data list
raw_data = [
    {"Name": "  rahul ", "City": " Delhi ", "Age": "25", "Salary": "40000", "Email": "RAHUL@GMAIL.COM"},
    {"Name": "Rahul", "City": "delhi", "Age": "25", "Salary": "40000", "Email": "rahul@gmail.com"},
    {"Name": "  Neha ", "City": "", "Age": "30", "Salary": "", "Email": " NEHA@EXAMPLE.COM "},
    {"Name": "Amit", "City": " Mumbai ", "Age": "28", "Salary": "52000", "Email": "amit@gmail.com"},
    {"Name": "Riya", "City": "Pune", "Age": "22", "Salary": "35000", "Email": "riya@gmail.com"},
]


def clean_text(value):
    if value is None:
        return ""
    return str(value).strip()


def clean_row(row):
    cleaned = {}

    for key, value in row.items():
        cleaned[key] = clean_text(value)

    # Standardize text values
    cleaned["Name"] = cleaned["Name"].title()
    cleaned["City"] = cleaned["City"].lower()
    cleaned["Email"] = cleaned["Email"].lower()

    # Convert Age and Salary to numbers if available
    if cleaned["Age"]:
        try:
            cleaned["Age"] = int(cleaned["Age"])
        except ValueError:
            cleaned["Age"] = None
    else:
        cleaned["Age"] = None

    if cleaned["Salary"]:
        try:
            cleaned["Salary"] = float(cleaned["Salary"])
        except ValueError:
            cleaned["Salary"] = None
    else:
        cleaned["Salary"] = None

    # Fill missing city with 'unknown'
    if not cleaned["City"]:
        cleaned["City"] = "unknown"

    return cleaned


cleaned_records = []
seen = set()

for row in raw_data:
    cleaned = clean_row(row)
    key = (cleaned["Name"], cleaned["Email"])

    if key in seen:
        continue

    seen.add(key)
    cleaned_records.append(cleaned)

print("Cleaned Data:")
for row in cleaned_records:
    print(row)

# Save to CSV
import csv

with open("cleaned_data_example.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "City", "Age", "Salary", "Email"])
    writer.writeheader()
    writer.writerows(cleaned_records)

print("\nSaved cleaned data to cleaned_data_example.csv")
