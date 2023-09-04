import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python remove_commas.py <input_csv> <output_csv>")
    sys.exit(1)

input_csv = sys.argv[1]
output_csv = sys.argv[2]

# Read the CSV file
data = pd.read_csv(input_csv)

# Remove commas from numbers in the entire dataframe
data = data.applymap(lambda x: str(x).replace(',', '') if isinstance(x, (int, float)) else x)

# Save the modified dataframe back to CSV
data.to_csv(output_csv, index=False)

print("Commas removed from numbers in the CSV file.")
