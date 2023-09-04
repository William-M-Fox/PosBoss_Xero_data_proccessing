import pandas as pd
from datetime import datetime

# Load the CSV file into a pandas DataFrame
data = pd.read_csv('cash_ups.csv')

print("Loaded CSV data:")
print(data.head())

# Define the time boundaries
half_before_time = datetime.strptime('05:00PM', '%I:%M%p').time()

# Function to categorize time
def categorize_time(row):
    if pd.isnull(row):
        return None
    elif row < half_before_time:
        return 'half'
    elif row >= half_before_time:
        return 'full'
    else:
        return None

# Convert 'Time' column to time objects
data['Time'] = data['Time'].apply(lambda x: datetime.strptime(x, '%I:%M%p').time() if pd.notnull(x) else None)

# Apply the categorize_time function to create the new column
data['Time_Category'] = data['Time'].apply(categorize_time)

print("\nData after time categorization:")
print(data.head())

seasons_mapping = {
    'Dec': 'Summer',
    'Jan': 'Summer',
    'Feb': 'Summer',
    'Mar': 'Autumn',
    'Apr': 'Autumn',
    'May': 'Autumn',
    'Jun': 'Winter',
    'Jul': 'Winter',
    'Aug': 'Winter',
    'Sep': 'Spring',
    'Oct': 'Spring',
    'Nov': 'Spring'
}

# Apply the seasons mapping to create a new 'Season' column
data['Season'] = data['Month'].map(seasons_mapping)

print("\nData after season mapping:")
print(data.head())

import requests

# Replace with your OpenWeatherMap API key
api_key = '0d205887184326764bdb5e708a969909'

# Define the location (Dunedin, New Zealand)
lat = -45.8788
lon = 170.5028



month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# Convert 'Month' column to numeric month
data['Month'] = data['Month'].map(month_mapping)

data['Year'] = 2000 + data['Year']

# Create the 'Date' column using 'Year', 'Month', and 'Day'
data['Date'] = pd.to_datetime(data[['Year', 'Month', 'Day']], errors='coerce')

# Convert the date to UNIX timestamp (required by OpenWeatherMap API)
data['timestamp'] = data['Date'].astype(int) / 10**9

# Fetch historical weather data for each date from the API
weather_data = []
for timestamp in data['timestamp']:
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}'
    
    # Print the URL for debugging purposes
    print("Fetching data from:", url)
    
    response = requests.get(url)
    weather_data.append(response.json())
    
    # Print the API response for debugging purposes
    print("API Response:", response.json())

# Extract temperature data and calculate daily average temperatures
daily_temps = []
for weather in weather_data:
    if 'hourly' in weather:
        hourly_temps = [entry['temp'] for entry in weather['hourly']]
        daily_temps.append(sum(hourly_temps) / len(hourly_temps))
    else:
        daily_temps.append(None)

# Add the calculated average temperatures to the DataFrame
data['Daily_Avg_Temp'] = daily_temps

# Save the modified DataFrame to a new CSV file
data.to_csv('data_with_temperatures.csv', index=False)