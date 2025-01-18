import pandas as pd

# Load the CSV files into pandas DataFrames
df_green = pd.read_csv('green_tripdata_2019-09.csv', low_memory=False)
df_lookup = pd.read_csv('taxi+_zone_lookup.csv')

# Convert timestamp columns to datetime format
df_green['lpep_pickup_datetime'] = pd.to_datetime(df_green['lpep_pickup_datetime'])

# Filter the green taxi dataset for pickups on September 18, 2019
pickup_date = '2019-09-18'
filtered_green = df_green[df_green['lpep_pickup_datetime'].dt.date == pd.to_datetime(pickup_date).date()]

# Merge with the taxi zone lookup dataset to get borough names
merged_df = pd.merge(filtered_green, df_lookup, how='left', left_on='PULocationID', right_on='LocationID')

# Define combinations of pickup boroughs
pickup_combinations = [
    ["Brooklyn", "Manhattan", "Queens"],
    ["Bronx", "Brooklyn", "Manhattan"],
    ["Bronx", "Manhattan", "Queens"],
    ["Brooklyn", "Queens", "Staten Island"]
]

# Initialize a dictionary to store the total amount for each combination
total_amounts = {}

# Iterate over each combination and calculate the total amount
for combination in pickup_combinations:
    # Filter the merged DataFrame for the current combination
    filtered_combination = merged_df[merged_df['Borough'].isin(combination)]
    
    # Calculate the total amount for the combination
    total_amount = filtered_combination['total_amount'].sum()
    
    # Store the result in the dictionary
    total_amounts[tuple(combination)] = total_amount

# Print the results
print("Total Amounts for Each Combination:")
for combination, total_amount in total_amounts.items():
    print(f"{combination}: {total_amount:.2f}")


# 75,"Manhattan","East Harlem South","Boro Zone"
# 76,"Brooklyn","East New York","Boro Zone"
# 145,"Queens","Long Island City/Hunters Point","Boro Zone"




# ('Brooklyn', 'Manhattan', 'Queens'): 267276.25
# "Brooklyn" "Manhattan" "Queens"
# "Bronx" "Brooklyn" "Manhattan"
# "Bronx" "Manhattan" "Queens"
# "Brooklyn" "Queens" "Staten Island"
