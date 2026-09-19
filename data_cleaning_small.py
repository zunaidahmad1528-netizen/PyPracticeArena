# Small Data Cleaning Example in Python

# Sample raw data
rows = [
    {"name": "  rahul ", "city": " Delhi ", "age": "25", "salary": "40000", "email": "RAHUL@GMAIL.COM"},
    {"name": "rahul", "city": "delhi", "age": "25", "salary": "40000", "email": "rahul@gmail.com"},
    {"name": "  Neha ", "city": "", "age": "30", "salary": "", "email": " NEHA@EXAMPLE.COM "},
    {"name": "Amit", "city": " Mumbai ", "age": "28", "salary": "52000", "email": "amit@gmail.com"},
]


def clean_value(value):
    if value is None:
        return ""
    return str(value).strip()


def is_missing(value):
    return clean_value(value) == ""


cleaned_rows = []
seen = set()

for row in rows:
    name = clean_value(row.get("name")).title()
    city = clean_value(row.get("city")).lower()
    email = clean_value(row.get("email")).lower()
    age = clean_value(row.get("age"))
    salary = clean_value(row.get("salary"))

    if not name:
        continue

    # Convert empty strings to None-like values
    if age:
        try:
            age = int(age)
        except ValueError:
            age = None
    else:
        age = None

    if salary:
        try:
            salary = float(salary)
        except ValueError:
            salary = None
    else:
        salary = None

    # Remove duplicate records using normalized name + email
    record_key = (name, email)
    if record_key in seen:
        continue
    seen.add(record_key)

    cleaned_rows.append({
        "name": name,
        "city": city or "unknown",
        "age": age,
        "salary": salary,
        "email": email,
    })

print("Cleaned Data:")
for item in cleaned_rows:
    print(item)

# Save cleaned data to a CSV file
import csv

fieldnames = ["name", "city", "age", "salary", "email"]
with open("cleaned_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

print("\nCSV file saved as cleaned_data.csv")
