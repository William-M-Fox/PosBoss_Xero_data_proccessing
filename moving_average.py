import pandas as pd
import sys

if len(sys.argv) != 4:
    print("Usage: python3 calculate_sma.py <input_csv> <output_csv> <window_size>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
window_size = int(sys.argv[3])

# Create a DataFrame from the input CSV file
df = pd.read_csv(input_file)

# Calculate a simple moving average with the specified window size
df['Moving Average'] = df['Turnover'].rolling(window=window_size).mean().round(2)

# Save the DataFrame with the moving average column to the output CSV file
df.to_csv(output_file, index=False)

print(f"Simple Moving Average with a window size of {window_size} calculated and saved to {output_file}.")
