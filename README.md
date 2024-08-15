# project-1
# Cta analysis

# Intro: This data analysis is meant to compare the amount of people who commute by bus and train in the busy city of Chicago. It also includes an minimum, maximum, and average of each respective ridership data. Furthermore, bar graphs and charts were used to better visualize trends in Cta commutes over the last 10 years. 

# Using the link https://rtams.org/services/cta/routes , I created a csv file to show how many bus routes run in Chicago. I used another csv that stored cta service dates, day type, bus riders, train riders, and total riders for that day, ranging from 2001 - present. I separated the data that I would be using from 2013-2023 and created another csv file to use in my code. 

# Solution: I imported the modules needed to properly run my code. Then I created a path to acess my csv files and stored them into pandas data frame. 

import csv
import pandas as pd
import datetime
from pathlib import Path

#Create path for bus route and ridership data
cta_bus_routes = Path(r"C:\Users\jasmi\OneDrive\Documents\Project-1\Resources\bus_routes.csv")
cta_riders = Path(r"C:\Users\jasmi\OneDrive\Documents\Project-1\Resources\ridership_2013_2023.csv")

#Store into pandas data frame
cta_bus_routes_df = pd.read_csv(cta_bus_routes)
cta_riders_df = pd.read_csv(cta_riders)

# I opened the bus route csv file and counted how many bus routes are located in Chicago. 
# Open and read bus route CSV file

with open(cta_bus_routes) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip header row and count the total number of votes recorded
#Calculate the total number of bus routes in Chicago

    next(csvreader)
    cta_bus_routes = list(csvreader)
    total_bus_routes = len(cta_bus_routes)

#print the total number of bus routes in Chicago
total_bus_routes

# To check the structure and contents of the cta_riders_df, I printed the head. 

#data frame contains cta data from 01/01/2013 - 12/31/2023
cta_riders_df['service_date'] = pd.to_datetime(cta_riders_df['service_date'])
cta_riders_df.head()

# I focused on bus riders in the last 10 years, calculating the total number of riders, lowest and highest number of riders recorded, and the average of bus riders. 

# Total number of bus riders
total_bus_riders = cta_riders_df['bus'].sum()
total_bus_riders
# Lowest number of bus riders
min_bus_riders = cta_riders_df['bus'].min()
min_bus_riders
# Highest number of bus riders
max_bus_riders = cta_riders_df['bus'].max()
max_bus_riders
# Average bus riders 
avg_bus_riders = cta_riders_df['bus'].mean()
avg_bus_riders

# Next, I calculated the same values for train riders in the last 10 years. 

# Total number of train riders 
total_train_riders = cta_riders_df['rail_boardings'].sum()
total_train_riders
# Lowest number of train riders
min_train_riders = cta_riders_df['rail_boardings'].min()
min_train_riders
# Average train riders 
avg_train_riders = cta_riders_df['rail_boardings'].mean()
avg_train_riders

# Finally, I calculated the average number of total riders in the last 10 years\

# Average of total cta riders
avg_cta_riders = cta_riders_df['total_rides'].mean()
avg_cta_riders
