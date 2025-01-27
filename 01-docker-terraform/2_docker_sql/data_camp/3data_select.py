import csv
from datetime import datetime

# Define the path to the CSV file
csv_file_path = 'green_tripdata_2019-10.csv'

# Define the distance ranges
distance_ranges = {
    'Up to 1 mile': 0,
    'Between 1 and 3 miles': 0,
    'Between 3 and 7 miles': 0,
    'Between 7 and 10 miles': 0,
    'Over 10 miles': 0
}

# Define the date range for the analysis
start_date = datetime.strptime('2019-10-01', '%Y-%m-%d')
end_date = datetime.strptime('2019-11-01', '%Y-%m-%d')

# Open and read the CSV file
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        pickup_date = datetime.strptime(row['lpep_pickup_datetime'], '%Y-%m-%d %H:%M:%S')
        trip_distance = float(row['trip_distance'])

        # Check if the trip is within the specified date range
        if start_date <= pickup_date < end_date:
            # Categorize the trip distance into the defined ranges
            if trip_distance <= 1:
                distance_ranges['Up to 1 mile'] += 1
            elif 1 < trip_distance <= 3:
                distance_ranges['Between 1 and 3 miles'] += 1
            elif 3 < trip_distance <= 7:
                distance_ranges['Between 3 and 7 miles'] += 1
            elif 7 < trip_distance <= 10:
                distance_ranges['Between 7 and 10 miles'] += 1
            else:
                distance_ranges['Over 10 miles'] += 1

# Print the results
for range_label, count in distance_ranges.items():
    print(f"{range_label}: {count} trips")
