import pandas as pd

# Load the CSV files into pandas DataFrames
df_green = pd.read_csv('green_tripdata_2019-09.csv', low_memory=False)
df_lookup = pd.read_csv('taxi+_zone_lookup.csv')

# Convert timestamp columns to datetime format
df_green['lpep_pickup_datetime'] = pd.to_datetime(df_green['lpep_pickup_datetime'])

# Merge with the taxi zone lookup dataset to get zone names
merged_df = pd.merge(df_green, df_lookup, how='left', left_on='PULocationID', right_on='LocationID')

# Filter for pickups in Astoria in September 2019
astoria_pickups = merged_df[(merged_df['Borough'] == 'Queens') & (merged_df['Zone'] == 'Astoria') & (merged_df['lpep_pickup_datetime'].dt.year == 2019) & (merged_df['lpep_pickup_datetime'].dt.month == 9)]

# Find the drop-off zone with the largest tip
largest_tip_dropoff = astoria_pickups.loc[astoria_pickups['tip_amount'].idxmax()]

# Get the name of the drop-off zone
dropoff_zone_name = df_lookup.loc[df_lookup['LocationID'] == largest_tip_dropoff['DOLocationID'], 'Zone'].values[0]

# Print the result
print(f"The drop-off zone with the largest tip for passengers picked up in Astoria in September 2019 is: {dropoff_zone_name}")
# The drop-off zone with the largest tip for passengers picked up in Astoria in September 2019 is: JFK Airport