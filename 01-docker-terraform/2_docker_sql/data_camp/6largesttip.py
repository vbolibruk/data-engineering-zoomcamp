import pandas as pd

# Load trip data
file_path = 'green_tripdata_2019-10.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Load taxi zone lookup table
zones_path = 'taxi_zone_lookup.csv'  # Replace with your file path
zones_df = pd.read_csv(zones_path)

# Map LocationID to Zone names
location_map = zones_df.set_index('LocationID')['Zone']

# Ensure datetime and filter for October 2019
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df_october = df[
    (df['lpep_pickup_datetime'] >= '2019-10-01') &
    (df['lpep_pickup_datetime'] < '2019-11-01')
]

# Filter for trips picked up in "East Harlem North"
east_harlem_north_id = zones_df[zones_df['Zone'] == 'East Harlem North']['LocationID'].values[0]
df_filtered = df_october[df_october['PULocationID'] == east_harlem_north_id]

# Find the drop-off zone with the largest tip
largest_tip_trip = df_filtered.loc[df_filtered['tip_amount'].idxmax()]
largest_tip_dolocation_id = largest_tip_trip['DOLocationID']
largest_tip_zone = location_map[largest_tip_dolocation_id]

# Display the result
print(f"The drop-off zone with the largest tip is: {largest_tip_zone}")
print(f"Largest tip amount: ${largest_tip_trip['tip_amount']:.2f}")
