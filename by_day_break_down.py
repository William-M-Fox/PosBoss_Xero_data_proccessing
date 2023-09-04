from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

# Define your login credentials or authentication process if needed
login_data = {
    'username': 'magpiecoffeedunedin@gmail.com',
    'password': 'iabbsdh13'
}

# Set up session with authentication
session = requests.Session()
login_url = 'https://posboss.com/login'
session.post(login_url, data=login_data)

# Define the URL pattern for historical data pages
base_url = 'https://app.posbosshq.com/app/history/transactions?start={date}T12%3A00%3A00.000Z&end={date}T12%3A00%3A00.000Z&range=day&taxType=taxInclusive'
dates = ['2022-09-03', '2022-09-04', '2022-09-10', '2022-09-11', '2022-09-17', '2022-09-18', '2022-09-24', '2022-09-25', '2022-10-01', '2022-10-02', '2022-10-08', '2022-10-09', '2022-10-15', '2022-10-16', '2022-10-22', '2022-10-23', '2022-10-29', '2022-10-30', '2022-11-05', '2022-11-06', '2022-11-12', '2022-11-13', '2022-11-19', '2022-11-20', '2022-11-26', '2022-11-27', '2022-12-03', '2022-12-04', '2022-12-10', '2022-12-11', '2022-12-17', '2022-12-18', '2022-12-24', '2022-12-25', '2022-12-31', '2023-01-01', '2023-01-07', '2023-01-08', '2023-01-14', '2023-01-15', '2023-01-21', '2023-01-22', '2023-01-28', '2023-01-29', '2023-02-04', '2023-02-05', '2023-02-11', '2023-02-12', '2023-02-18', '2023-02-19', '2023-02-25', '2023-02-26', '2023-03-04', '2023-03-05', '2023-03-11', '2023-03-12', '2023-03-18', '2023-03-19', '2023-03-25', '2023-03-26', '2023-04-01', '2023-04-02', '2023-04-08', '2023-04-09', '2023-04-15', '2023-04-16', '2023-04-22', '2023-04-23', '2023-04-29', '2023-04-30', '2023-05-06', '2023-05-07', '2023-05-13', '2023-05-14', '2023-05-20', '2023-05-21', '2023-05-27', '2023-05-28', '2023-06-03', '2023-06-04', '2023-06-10', '2023-06-11', '2023-06-17', '2023-06-18', '2023-06-24', '2023-06-25', '2023-07-01', '2023-07-02', '2023-07-08', '2023-07-09', '2023-07-15', '2023-07-16', '2023-07-22', '2023-07-23', '2023-07-29', '2023-07-30', '2023-08-05', '2023-08-06', '2023-08-12', '2023-08-13', '2023-08-19', '2023-08-20', '2023-08-26', '2023-08-27', '2023-09-02', '2023-09-03']  # Replace with your desired dates

# Initialize a list to store extracted data
extracted_data = []

# Iterate through the list of dates and scrape data from each page
for date in dates:
    date_url = f'{base_url}{date}'
    response = session.get(date_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <div> elements with the class 'flex justify-between items-center'
        order_details_divs = soup.find_all('div', class_='flex justify-between items-center')
        
        # Extract the time and dollar amount from each <div> element
        for div in order_details_divs:
            order_details_text = div.find(text=True, recursive=False)
            if order_details_text:
                # Check if the text contains both time and dollar amount
                if ':' in order_details_text and '$' in order_details_text:
                    time, dollar_amount = order_details_text.split('$', 1)
                    extracted_data.append({'date': date, 'time': time.strip(), 'amount': f'${dollar_amount.strip()}'})

    else:
        print(f"Failed to retrieve data for {date}")

# Print the extracted data
for entry in extracted_data:
    print(f"Date: {entry['date']}, Time: {entry['time']}, Amount: {entry['amount']}")

# Close the session
session.close()
