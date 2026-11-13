# CSV Doctor

A small Python command-line tool that cleans a CSV file by trimming whitespace, standardizing column names, removing completely blank rows, and removing exact duplicate rows. It also writes a JSON report.

**Portfolio status:** Independent demonstration using synthetic data. It is not a commissioned client project.

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run the demonstration

```bash
python generate_data.py
python csv_doctor.py
```

Expected files:

- `messy_customers.csv` — generated sample input
- `cleaned_customers.csv` — cleaned output
- `cleaned_customers.report.json` — processing summary

## Clean another CSV

```bash
python csv_doctor.py path/to/input.csv --output cleaned.csv
```

## What it does

1. Reads a CSV file with UTF-8 or UTF-8 BOM encoding.
2. Trims spaces from values.
3. Converts column names to lowercase with underscores.
4. Removes completely blank rows.
5. Removes exact duplicate rows.
6. Saves a JSON report with row counts and output columns.

## Limits

- Duplicate removal compares the complete row. It does not decide whether two similar customer records are the same person.
- It does not guess missing values or change business meaning.
- Review the output before using it for business decisions.

## Reproducibility

The generator uses a fixed random seed, so it creates the same sample data each time.

## License

MIT. See `LICENSE` if you add one before public distribution.
