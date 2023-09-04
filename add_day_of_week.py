import csv
from datetime import datetime
import sys

if len(sys.argv) != 3:
    print("Usage: python3 add_day_of_week <input_csv> <output_file>")
    sys.exit(1)

# Function to get the day of the week as a string
def get_day_of_week(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj.strftime('%A')

# Input and output file paths
input_file = sys.argv[1]
input_csv = input_file
output_file = sys.argv[2]
output_csv = output_file

# Read the CSV file
with open(input_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

# Add a new row with headers for the day of the week
data[0].append('Day of the Week')

# Iterate through the rows (starting from the second row) and add the day of the week
for row in data[1:]:
    date_column = row[0]
    day_of_week = get_day_of_week(date_column)
    row.append(day_of_week)

# Write the updated data to a new CSV file
with open(output_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f'Day of the week added to {output_csv}')
