from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Calculate the start date as one year ago from today
start_date = current_date - timedelta(days=365)

# Initialize a list to store weekend dates
weekend_dates = []

# Iterate through the date range and check for weekends
while start_date <= current_date:
    # Check if the current day is a thursday friday or saturday
    if start_date.weekday() in [3, 4, 5]:
        weekend_dates.append(start_date.strftime("'%Y-%m-%d'"))
    
    # Move to the next day
    start_date += timedelta(days=1)

# Print the list of weekend dates with commas
print(', '.join(weekend_dates))
