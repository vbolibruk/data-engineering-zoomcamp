import pandas as pd

# Load data from file
file_path = 'green_tripdata_2019-10.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Ensure the pickup datetime column is in datetime format
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])

# Extract the date part from the pickup datetime
df['pickup_date'] = df['lpep_pickup_datetime'].dt.date

# Find the longest trip for each day
longest_trips = df.loc[df.groupby('pickup_date')['trip_distance'].idxmax()]

# Find the pick-up day with the longest trip distance overall
longest_trip_day = longest_trips.loc[longest_trips['trip_distance'].idxmax()]

# Display the result
print("Longest trip for each day:")
print(longest_trips[['pickup_date', 'trip_distance']])

print("\nDay with the overall longest trip:")
print(longest_trip_day[['pickup_date', 'trip_distance']])
