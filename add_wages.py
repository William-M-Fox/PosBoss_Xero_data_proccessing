import pandas as pd
import sys

if len(sys.argv) != 4:
    print("Usage: python merge_files.py <file1_csv> <file2_csv> <output_csv>")
    sys.exit(1)

file1_csv = sys.argv[1]
file2_csv = sys.argv[2]
output_csv = sys.argv[3]

# Read the CSV files into pandas DataFrames
file1 = pd.read_csv(file1_csv)
file2 = pd.read_csv(file2_csv)

# Merge based on two columns from file1 and file2
merged_data = pd.merge(file1, file2, left_on=['Month', 'Year'], right_on=['Month', 'Year'], how='left')

# Save the merged DataFrame to a new CSV file
merged_data.to_csv(output_csv, index=False)
