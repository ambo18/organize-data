import pandas as pd

# Initialize an empty list to store the organized data
organized_data = []

# Open and read the text file
with open('OPD_records.txt', 'r') as file:
    # Read all lines
    lines = file.readlines()
    
    # Process each line
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces
        
        # If the line contains 'SDH #' (hospital number)
        if "SDH #" in line:
            # Split the line into name and hospital number at the first occurrence of 'SDH #'
            name_part, hospital_number = line.split('SDH #', 1)
            hospital_number = 'SDH #' + hospital_number.strip()  # Format the hospital number
            
            # Split the name part into individual name components
            name_parts = name_part.split(",")
            
            # Handle cases where the name part has two or three components (Last, First, and Middle)
            if len(name_parts) == 2:
                last_name = name_parts[0].strip()
                first_name = name_parts[1].strip()
                middle_name = ""  # No middle name
            else:
                last_name = name_parts[0].strip()
                first_name = name_parts[1].strip()
                middle_name = name_parts[2].strip() if len(name_parts) > 2 else ""
            
            # Append the organized data
            organized_data.append([last_name, first_name, middle_name, hospital_number])
        
        # If the line does not contain 'SDH #' (incomplete record)
        else:
            name_parts = line.split(",")
            if len(name_parts) == 2:
                last_name = name_parts[0].strip()
                first_name = name_parts[1].strip()
                middle_name = ""
                hospital_number = ""
            elif len(name_parts) == 3:
                last_name = name_parts[0].strip()
                first_name = name_parts[1].strip()
                middle_name = name_parts[2].strip()
                hospital_number = ""
            else:
                last_name = first_name = middle_name = hospital_number = ""
            
            # Append the organized data without hospital number
            organized_data.append([last_name, first_name, middle_name, hospital_number])

# Convert the organized data into a DataFrame
df = pd.DataFrame(organized_data, columns=["Last Name", "First Name", "Middle Name", "Hospital Number"])

# Save the DataFrame to an Excel file
df.to_excel("organized_data.xlsx", index=False)

# Output confirmation message
print("Data has been organized and saved to 'organized_data.xlsx'.")
