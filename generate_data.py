"""Create a deliberately messy sample customer CSV for CSV Doctor."""
import csv
import random
from pathlib import Path

random.seed(7)
OUTPUT = Path("messy_customers.csv")

first_names = ["Ava", "Noah", "Mia", "Liam", "Zara", "Ethan", "Iris", "Omar"]
last_names = ["Khan", "Smith", "Patel", "Brown", "Ali", "Garcia"]
cities = ["London", "Lahore", "Toronto", "Berlin", "Dubai"]

rows = []
for number in range(1, 101):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first.lower()}.{last.lower()}{number}@example.com"
    row = {
        " Customer ID ": f" C{number:04d} ",
        "Name": f" {first} {last} ",
        " Email ": email,
        "City": f" {random.choice(cities)} ",
        "Status": random.choice([" active ", "inactive", " Active", "pending "]),
    }
    if number % 13 == 0:
        row[" Email "] = "   "
    if number % 17 == 0:
        row["City"] = ""
    rows.append(row)

# Add exact duplicate rows to test duplicate removal.
rows.extend([rows[4].copy(), rows[19].copy(), rows[49].copy()])
rows.insert(25, {key: "" for key in rows[0]})  # Add one completely blank row.

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {OUTPUT} with {len(rows)} data rows.")
