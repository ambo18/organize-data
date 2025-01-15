import re
import pandas as pd

# Read data from the document file
with open("OPD_records.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Regular expression to parse the data
pattern = re.compile(r"(?P<last_name>[A-Z]+), (?P<first_name>[A-Z]+(?: [A-Z]+)*)(?: (?P<middle_name>[A-Z. ]+))? (SDH# \d+)?")

# List to hold structured data
entries = []

# Process each match
for match in pattern.finditer(data):
    last_name = match.group("last_name")
    first_name = match.group("first_name")
    middle_name = match.group("middle_name") or ""
    hospital = match.group(4) or ""
    entries.append({
        "Last Name": last_name,
        "First Name": first_name,
        "Middle Name": middle_name.strip(),
        "Hospital": hospital.strip(),
    })

# Convert to DataFrame
df = pd.DataFrame(entries)

# Save to Excel
output_file = "organized_data.xlsx"
df.to_excel(output_file, index=False)

print(f"Data has been organized and saved to {output_file}")
