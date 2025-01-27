import pandas as pd

# Load the data from the CSV file
file_path = 'green_tripdata_2019-10.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Ensure datetime and filter by 2019-10-18
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df_filtered = df[df['lpep_pickup_datetime'].dt.date == pd.to_datetime('2019-10-18').date()]

# Group by pickup location (PULocationID) and sum the total_amount
pickup_totals = df_filtered.groupby('PULocationID')['total_amount'].sum()

# Filter locations with total_amount > 13,000
top_pickups = pickup_totals[pickup_totals > 13000].sort_values(ascending=False)

# Display the top pickup locations
print("Top pickup locations with total_amount > 13,000 for 2019-10-18:")
print(top_pickups)
