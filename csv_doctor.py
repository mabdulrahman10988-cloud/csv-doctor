"""Clean a CSV file and write a JSON quality report using only Python's standard library."""
import argparse
import csv
import json
import re
from pathlib import Path


def clean_header(value):
    """Trim a column name and replace internal spaces with underscores."""
    value = re.sub(r"\s+", "_", value.strip())
    return value.lower()


def main():
    parser = argparse.ArgumentParser(description="Clean whitespace, blank rows and duplicate rows in a CSV.")
    parser.add_argument("input", nargs="?", default="messy_customers.csv", help="Input CSV path")
    parser.add_argument("--output", default="cleaned_customers.csv", help="Output CSV path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    report_path = output_path.with_suffix(".report.json")

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}. Run: python generate_data.py")

    with input_path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise SystemExit("The input CSV has no header row.")
        original_headers = reader.fieldnames
        clean_headers = [clean_header(name) for name in original_headers]
        rows = list(reader)

    seen = set()
    cleaned_rows = []
    duplicate_rows = 0
    blank_rows = 0

    for raw_row in rows:
        values = [str(raw_row.get(header, "") or "").strip() for header in original_headers]
        if not any(values):
            blank_rows += 1
            continue
        row_key = tuple(values)
        if row_key in seen:
            duplicate_rows += 1
            continue
        seen.add(row_key)
        cleaned_rows.append(dict(zip(clean_headers, values)))

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=clean_headers)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    report = {
        "input_file": str(input_path),
        "output_file": str(output_path),
        "input_data_rows": len(rows),
        "output_data_rows": len(cleaned_rows),
        "duplicate_rows_removed": duplicate_rows,
        "blank_rows_removed": blank_rows,
        "columns": clean_headers,
        "whitespace_trimmed": True,
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Input rows: {len(rows)}")
    print(f"Output rows: {len(cleaned_rows)}")
    print(f"Duplicates removed: {duplicate_rows}")
    print(f"Blank rows removed: {blank_rows}")
    print(f"Saved: {output_path}")
    print(f"Saved: {report_path}")


if __name__ == "__main__":
    main()
