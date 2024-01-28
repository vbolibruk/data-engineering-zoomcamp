import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('green_tripdata_2019-09.csv')

# Convert timestamp columns to datetime format
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

# Filter the dataset for trips on September 18th, 2019
sept_18_trips = df[(df['lpep_pickup_datetime'].dt.date == pd.to_datetime('2019-09-18').date()) & 
                   (df['lpep_dropoff_datetime'].dt.date == pd.to_datetime('2019-09-18').date())]

# Get the total number of trips
num_trips_sept_18 = len(sept_18_trips)

print(f'Total number of taxi trips on September 18th, 2019: {num_trips_sept_18}')
# Total number of taxi trips on September 18th, 2019: 15612