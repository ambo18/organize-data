import pandas as pd
import re

# Function to process and organize data
def process_data(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = infile.read()

    # Regex to match Full Name (Last, First, and Middle Name) and Hospital Number
    pattern = r"([A-Za-z\-]+),\s([A-Za-z\s\-]+)(?:\s([A-Za-z\s\-]+))?\s(SDH #\s\d+)"
    matches = re.findall(pattern, data)

    # Prepare the rows for DataFrame with Full Name and Hospital Number
    rows = []
    for match in matches:
        last_name, first_name, middle_name, hospital_number = match
        # Combine full name (Last, First, Middle if available)
        full_name = f"{last_name}, {first_name} {middle_name if middle_name else ''}".strip()
        rows.append([full_name, hospital_number])

    # Create a DataFrame with Full Name and Hospital Number columns
    df = pd.DataFrame(rows, columns=['Full Name', 'Hospital Number'])

    # Write to an Excel file
    df.to_excel(output_file, index=False)

    print(f"Data has been processed and saved to '{output_file}'.")

# Input and output file paths
input_file = 'OPD_records.txt'
output_file = 'formatted_OPD_records.xlsx'

# Process the data
process_data(input_file, output_file)
