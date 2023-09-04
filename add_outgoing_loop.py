import pandas as pd
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python process_outgoings.py <input_csv>")
    sys.exit(1)

input_file = sys.argv[1]

# Read the initial input file
output_data = pd.read_csv(input_file)

# Get the current working directory
current_directory = os.getcwd()

# List all CSV files in the current directory
outgoing_files = [file for file in os.listdir(current_directory) if file.endswith(".csv")]

for outgoing_file in outgoing_files:
    result_string = os.path.splitext(os.path.basename(outgoing_file))[0]
    
    file2 = pd.read_csv(os.path.join(current_directory, outgoing_file), skiprows=6, delimiter=',')
    file2['payee_' + result_string] = file2.iloc[:, 2]
    file2['gross_' + result_string] = file2.iloc[:, 7]
    # Clean and convert 'gross' values to numeric (filter out non-numeric values)
    file2['gross_' + result_string] = file2['gross_' + result_string].str.replace(',', '', regex=True)
    file2['gross_' + result_string] = pd.to_numeric(file2['gross_' + result_string], errors='coerce')

    # Remove rows with non-numeric values in the 'gross' column 
    file2 = file2.dropna(subset=['gross_' + result_string])


    # Filter out rows that don't have a valid date in the first column of file2
    valid_dates = pd.to_datetime(file2.iloc[:, 0], format='%d %b %Y', errors='coerce')
    file2 = file2[valid_dates.notna()]
    file2['Date'] = valid_dates
    

    # Group and sum the 'gross' values in file2 based on the 'Date'
    file2_grouped = file2.groupby('Date')['gross_' + result_string].sum().reset_index()

    # Group the 'payee' values in file2 based on the 'Date' and concatenate with semicolons
    file2_payee_grouped = file2.groupby('Date')['payee_' + result_string].apply(lambda x: ';'.join(x)).reset_index()

    # Merge the grouped dataframes with the output_data
    output_data['Date'] = pd.to_datetime(output_data['Date'])
    output_data = pd.merge(output_data, file2_grouped, on='Date', how='left')
    output_data = pd.merge(output_data, file2_payee_grouped, on='Date', how='left')

# Save the merged data to the final output file
final_output_file = "final_merged_output.csv"
output_data.to_csv(final_output_file, index=False)
