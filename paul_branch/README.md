# project-1
### Bus Tracker
This script serves as both data collection and visualization. Using the CTA Bus Tracker API, I pulled the ID of one bus from every bus route. Then, over various points in the week of August 8th, I tracked the Latitude and Longitude of one bus from every route every minute for an hour. I then used the haversine equation to convert this to miles. Once this was done, I made an hvplot showing the locations of the buses on August 8th, bar charts showing the 10 slowest and fastest bus routes, and distribution and box plots comparing the express vs the non-express lines

#### output
This directory contains images of the charts and the route_info csv that contains info about every bus route

#### output/bus_locations
This directory contains the data pulled from the Bus Tracker API on August 8th,, 10th, 11th, and 12th at different times of the day.


All of the code is originally mine, with the exception of a few times I needed help from the internet. All of these are credited within the comments of bus_tracker.ipynb