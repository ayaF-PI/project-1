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
# Median bus rider data
med_bus_riders = cta_riders_df['bus'].median()
med_bus_riders
# Bus rider dataset Quartiles
data = pd.Series(cta_riders_df['bus'])
bus_quartiles = data.quantile([0.25,0.5,0.75])
bus_quartiles
# Bus rider dataset outliers
#  Bus rider dataset variable
bus_data_o = cta_riders_df['bus']

# Calculate Q1, Q3, and IQR
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# Calculate lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = [x for x in data if x < lower_bound or x > upper_bound]

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", outliers)

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
# Median train rider data
med_train_riders = cta_riders_df['rail_boardings'].median()
med_train_riders
# Train rider qurtiles in dataset
data = pd.Series(cta_riders_df['rail_boardings'])
train_quartiles = data.quantile([0.25,0.5,0.75])
train_quartiles

# Train rider outliers
# Train rider dataset variable
train_data_o = cta_riders_df['rail_boardings']

# Calculate Q1, Q3, and IQR
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# Calculate lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = [x for x in data if x < lower_bound or x > upper_bound]

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", outliers)
# Finally, I calculated the average number of total riders in the last 10 years\

# Average of total cta riders
avg_cta_riders = cta_riders_df['total_rides'].mean()
avg_cta_riders
# After these statistical values were calculated for both train and bus riders, and their totals, I proceeded to create box and whisker plots to represent each data set in a seperate file.

# Solution :

# I imported the modules needed to create the data visuals. 

%matplotlib notebook 
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

# I created a path for bus route and ridership data
cta_bus_routes = Path(r"C:\Users\jasmi\OneDrive\Documents\Project-1\Resources\bus_routes.csv")
cta_riders = Path(r"C:\Users\jasmi\OneDrive\Documents\Project-1\Resources\ridership_2013_2023.csv")

# Stored into pandas data frame
cta_bus_routes_df = pd.read_csv(cta_bus_routes)
cta_riders_df = pd.read_csv(cta_riders)

# To create my box plot, I created a variable for the bus rider data (min, quartiles, mean, max)
bus_data = [80783, 375720.5, 539617.0, 829277.5, 1100251]

#Create a boxplot to represent data
plt.boxplot(bus_data,whis=1.5, showmeans=True, meanline=True)
plt.title('Bus Rider Stats. 2013-2023')
plt.xlabel('Bus Riders')
plt.ylabel('Data Distribution')
plt.show()

# Next I did the same for the train rider dataset. I created a variable for the calculated figures done previously

#Create a variable for train data (min, quartiles, mean, max)
train_data = [23544, 296012.0, 456039.0, 743390.0, 1146516]

#Create a box plot to visualize data
plt.boxplot(train_data,whis=1.5, showmeans=True, meanline=True)
plt.title('Train Rider Stats. 2013-2023')
plt.xlabel('Train Riders')
plt.ylabel('Data Distribution')
plt.show()

# Finally, I created a pie chart to compare the total number of riders that have commuted by bus and train in the last 10 years. The 'sizes' values are the total number of train and bus riders taken from the dataset. 

#Define data for pie chart
sizes = [2400569460, 2017341062]
labels = ['Bus Commuters', 'Train Commuters' ]
colors = ['xkcd:sky blue','cyan']
pie_title_font =  {'family': 'serif', 'color':'black', 'weight':'light', 'size': 16}
explode = (0, 0.1)  

# Create the pie chart
# Comparing total riders that commute by bus and trains in last 10 years
plt.pie(sizes, labels=labels, explode=explode, labeldistance=.3, colors=colors, shadow=True, autopct='%1.1f%%')
plt.axis('equal')  
plt.title('Chicago Transit Analysis', fontdict= pie_title_font)
plt.show()

# Conclusion: Between the years 2013-2023, there were more people recorded commuting by bus than train in Chicago. Weaknesses in the data would include riders who do not scan cta card, free transfers between stations/buses, and cta scanners that are out of service unable to properly record passengers.
