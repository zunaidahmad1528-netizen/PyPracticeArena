"""A practical data-cleaning example using only Python's standard library."""

from __future__ import annotations

import csv
import re
from datetime import datetime
from pathlib import Path
from typing import Any


RAW_CUSTOMERS: list[dict[str, Any]] = [
    {
        "name": "  mohd zunaid ",
        "email": " ZUNAID@EXAMPLE.COM ",
        "phone": "+91 98765-43210",
        "age": "22",
        "city": " lucknow ",
        "joined": "2025/01/15",
    },
    {
        "name": "Aisha Khan",
        "email": "aisha@example.com",
        "phone": "9876543211",
        "age": "unknown",
        "city": "Delhi",
        "joined": "15-02-2025",
    },
    {
        "name": "Aisha Khan",
        "email": "aisha@example.com",
        "phone": "9876543211",
        "age": "unknown",
        "city": "Delhi",
        "joined": "15-02-2025",
    },
    {
        "name": "  rahul sharma",
        "email": "rahul@example",
        "phone": "not available",
        "age": "31",
        "city": "mumbai",
        "joined": "2025-03-01",
    },
]


def clean_text(value: Any) -> str:
    """Remove extra whitespace and use a consistent case for text values."""
    return " ".join(str(value or "").split()).strip().title()


def clean_email(value: Any) -> str | None:
    """Normalize an email and return None when it is not valid."""
    email = str(value or "").strip().lower()
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return email if re.fullmatch(pattern, email) else None


def clean_phone(value: Any) -> str | None:
    """Keep digits only and format a 10-digit phone number."""
    digits = re.sub(r"\D", "", str(value or ""))
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return f"+91 {digits[:5]}-{digits[5:]}" if len(digits) == 10 else None


def clean_age(value: Any) -> int | None:
    """Convert an age to an integer and reject unrealistic values."""
    try:
        age = int(value)
    except (TypeError, ValueError):
        return None
    return age if 0 < age < 130 else None


def clean_date(value: Any) -> str | None:
    """Convert common date formats to ISO format: YYYY-MM-DD."""
    for date_format in ("%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value).strip(), date_format).date().isoformat()
        except ValueError:
            continue
    return None


def clean_customer(record: dict[str, Any]) -> dict[str, Any]:
    """Clean one customer record and fill missing values consistently."""
    return {
        "name": clean_text(record.get("name")) or "Unknown",
        "email": clean_email(record.get("email")) or "missing@example.com",
        "phone": clean_phone(record.get("phone")) or "Not available",
        "age": clean_age(record.get("age")),
        "city": clean_text(record.get("city")) or "Unknown",
        "joined": clean_date(record.get("joined")) or "Unknown",
    }


def remove_duplicates(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Remove duplicate records by normalized email."""
    unique_records: dict[str, dict[str, Any]] = {}
    for record in records:
        unique_records.setdefault(record["email"], record)
    return list(unique_records.values())


def validate_records(records: list[dict[str, Any]]) -> list[str]:
    """Return readable validation errors without stopping the whole pipeline."""
    errors: list[str] = []
    for row_number, record in enumerate(records, start=1):
        if record["email"] == "missing@example.com":
            errors.append(f"Row {row_number}: email missing or invalid")
        if record["age"] is None:
            errors.append(f"Row {row_number}: age missing or invalid")
        if record["phone"] == "Not available":
            errors.append(f"Row {row_number}: phone missing or invalid")
    return errors


def save_csv(records: list[dict[str, Any]], filename: str = "clean_customers.csv") -> Path:
    """Export cleaned records to a CSV file."""
    output_path = Path(filename)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)
    return output_path


def main() -> None:
    cleaned_records = [clean_customer(record) for record in RAW_CUSTOMERS]
    cleaned_records = remove_duplicates(cleaned_records)
    validation_errors = validate_records(cleaned_records)

    print(f"Raw records: {len(RAW_CUSTOMERS)}")
    print(f"Clean records: {len(cleaned_records)}")
    print("\nCleaned data:")
    for record in cleaned_records:
        print(record)

    print("\nValidation report:")
    if validation_errors:
        print("\n".join(f"- {error}" for error in validation_errors))
    else:
        print("No problems found")

    output_path = save_csv(cleaned_records)
    print(f"\nCSV saved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
