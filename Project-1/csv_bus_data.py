import os
import csv
import pandas as pd
from datetime import date

csv_bus_routes = r"C:\Users\jasmi\OneDrive\Documents\Project-1\Resources\CTA_-_Bus_Routes_20240811.csv"

with open(csv_bus_routes) as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    bus_routes = list(csvreader)
    total_bus_routes = len(bus_routes)

print(total_bus_routes)

csv_ridership = r"C:\Users\jasmi\OneDrive\Documents\Project-1\Resources\CTA_-_Ridership_-_Daily_Boarding_Totals_20240812.csv"
 
# Variables
service_date = []
bus = []
total_rides = []

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_ridership)    

# Convert the date column to DateTime format
df[service_date] = pd.to_datetime(df[service_date])

# Define the date range you want to filter
start_date = [2013,01,01]
end_date = [2023,12,31]

# Filter the data based on the date range
filtered_data = df[(df[service_date] >= start_date) & (df[service_date] <= end_date)]

# Display the filtered data
print(filtered_data)