# Example file for Advanced Python: Hands On by Joe Marini
# Using the reduce function

import json
import pprint
from functools import reduce


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?
#pprint.pp(weatherdata)
# print(sum(map(lambda x:x["snow"],weatherdata)))
total_snow = reduce(lambda acc, x: acc + x["snow"],weatherdata,0)
print(total_snow)
 
# TODO: how much total precipitation is in the entire dataset?
# print(sum(map(lambda x:x["prcp"]+x["snow"],weatherdata)))
total_precip = reduce(lambda acc,x:acc+x["snow"]+x["prcp"],weatherdata,0)
print(total_precip)

# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0
#print(max(filter(lambda x:x["snow"]>0, weatherdata),key=lambda y:y["tmax"]))

# def warm_snow_day(acc, elem):
#     # return the elem value if the snow amount > 0 and its tmax value is
#     # larger than the tmax value that is in the acc argument
#     return elem if elem["snow"] > 0 and elem["tmax"] > acc["tmax"] else acc

# define a "zero" value start date for the reduce function to start with
start_val = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
}


# TODO: reduce the data set to the warmest snow day
# reduced = reduce(warm_snow_day,weatherdata)
# pprint.pp(reduced)