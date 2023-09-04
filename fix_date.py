import pandas as pd

# Read the CSV file
data = pd.read_csv("output_file.csv")

# Define the input date format
input_format = "%d/%m/%y"

# Convert the date column to a standardized format
data['Date'] = pd.to_datetime(data['Date'], format=input_format).dt.strftime('%Y-%m-%d')

# Save the modified data to a new CSV file
data.to_csv("maggies_final.csv", index=False)
