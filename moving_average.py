import pandas as pd


# Create a DataFrame from the sample data
df = pd.read_csv("full_data.csv")

# Calculate a simple moving average with a window size of 3
window_size = 90
df['Moving Average'] = df['Turnover'].rolling(window=window_size).mean().round(2)

# Print the DataFrame with the SMA column
df.to_csv("maggies_final.csv", index=False)