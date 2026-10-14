import argparse
from pathlib import Path

import pandas as pd


def clean_text_series(series):
    """Trim spaces and convert empty values to None/Unknown."""
    cleaned = series.astype(str).str.strip()
    cleaned = cleaned.replace({'nan': None, 'None': None, '': None})
    return cleaned


def clean_dataframe(df):
    """Clean a messy Excel dataset."""
    df = df.copy()

    # Standardize column names
    df.columns = [str(col).strip().lower().replace(' ', '_') for col in df.columns]

    # Remove completely empty rows
    df = df.dropna(how='all')

    # Clean text columns
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = clean_text_series(df[col])

    # Standardize some common text fields
    for col in ['name', 'city', 'email', 'customer_name', 'state']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].str.replace(r'\s+', ' ', regex=True)

    if 'name' in df.columns:
        df['name'] = df['name'].str.title()
    if 'city' in df.columns:
        df['city'] = df['city'].str.lower()
    if 'email' in df.columns:
        df['email'] = df['email'].str.lower()
    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.strip().str.lower()

    # Convert numeric columns
    numeric_columns = ['age', 'salary', 'amount', 'total', 'price', 'qty', 'quantity']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill missing values in text columns
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].replace({None: 'Unknown', 'nan': 'Unknown', 'None': 'Unknown'})

    # Fill missing numeric values with 0
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)

    # Remove duplicates based on available key columns
    key_columns = []
    for candidate in ['email', 'name', 'customer_name', 'phone']:
        if candidate in df.columns:
            key_columns.append(candidate)

    if len(key_columns) >= 1:
        df = df.drop_duplicates(subset=key_columns, keep='first')

    df = df.reset_index(drop=True)
    return df


def main():
    parser = argparse.ArgumentParser(description='Clean messy Excel/CSV data using pandas.')
    parser.add_argument('input_file', help='Path to the Excel or CSV file to clean')
    parser.add_argument('--output', '-o', default=None, help='Output file name. Default: cleaned_<input>.xlsx')
    args = parser.parse_args()

    input_path = Path(args.input_file)

    if not input_path.exists():
        print(f"Error: file not found: {input_path}")
        return

    suffix = input_path.suffix.lower()

    try:
        if suffix == '.csv':
            df = pd.read_csv(input_path)
        else:
            df = pd.read_excel(input_path)
    except Exception as exc:
        print(f"Error reading file: {exc}")
        return

    cleaned_df = clean_dataframe(df)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_name(f"cleaned_{input_path.stem}.xlsx")

    if output_path.suffix.lower() == '.csv':
        cleaned_df.to_csv(output_path, index=False)
    else:
        cleaned_df.to_excel(output_path, index=False)

    print(f"Original rows: {len(df)}")
    print(f"Cleaned rows: {len(cleaned_df)}")
    print(f"Saved cleaned file to: {output_path}")

    csv_output = output_path.with_suffix('.csv')
    cleaned_df.to_csv(csv_output, index=False)
    print(f"CSV copy saved to: {csv_output}")


if __name__ == '__main__':
    main()
