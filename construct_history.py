import pandas as pd

# Read the list of dates from dates.txt and split it into a list
with open('dates.txt', 'r') as date_file:
    dates_str = date_file.read()
    dates_list = [date.strip("' ") for date in dates_str.split(',')]

# Load the CSV data into a pandas DataFrame, specifying a placeholder for missing fields
df = pd.read_csv('six_month_history.csv', header=None, names=['Timestamp', 'Type', 'Payment', 'Card', 'Customer', 'Till', 'Amount1', 'Amount2'], skiprows=1, na_values=[''])

# Convert the 'Timestamp' column to datetime, and handle errors
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d %b %Y %I:%M%p', errors='coerce')

# Filter out rows with invalid 'Timestamp' values
df = df[df['Timestamp'].notna()]

# Preprocess the data: If the second to last field is a number with a decimal, delete the last field
def is_numeric_with_decimal(value):
    if isinstance(value, str):
        try:
            float(value)
            return '.' in value
        except ValueError:
            return False
    return False

df['Amount1'] = df.apply(lambda row: row['Amount2'] if is_numeric_with_decimal(row['Amount2']) else row['Amount1'], axis=1)
df = df.drop(columns=['Amount2'])

# Convert the list of dates to datetime objects
dates_datetime = pd.to_datetime(dates_list, format='%Y-%m-%d')

# Filter the DataFrame to include only rows with dates from the list
filtered_df = df[df['Timestamp'].dt.date.isin(dates_datetime.date)]

# Define a function to classify the time as 'Day' or 'Night'
def classify_time(timestamp):
    if timestamp.hour < 16:  # Before 4:00 PM
        return 'Day'
    else:
        return 'Night'

# Apply the time classification function to the DataFrame using .loc
filtered_df = filtered_df.copy()
filtered_df.loc[:, 'TimeOfDay'] = filtered_df['Timestamp'].apply(classify_time)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_history.csv', index=False)

