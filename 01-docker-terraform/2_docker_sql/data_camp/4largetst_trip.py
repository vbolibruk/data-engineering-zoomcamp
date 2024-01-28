import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('green_tripdata_2019-09.csv')

# Convert timestamp columns to datetime format
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])

# Filter the dataset for each specified date and calculate the total trip distance for each day
dates = ['2019-09-18', '2019-09-16', '2019-09-26', '2019-09-21']

max_distance = 0
max_distance_day = None

for date in dates:
    trips_on_date = df[df['lpep_pickup_datetime'].dt.date == pd.to_datetime(date).date()]
    total_distance = trips_on_date['trip_distance'].sum()
    
    if total_distance > max_distance:
        max_distance = total_distance
        max_distance_day = date

print(f'The pickup day with the largest total trip distance is {max_distance_day} with a distance of {max_distance:.2f} miles.')
# The pickup day with the largest total trip distance is 2019-09-26 with a distance of 58759.94 miles.