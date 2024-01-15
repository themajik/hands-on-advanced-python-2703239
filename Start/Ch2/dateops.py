# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json
from datetime import datetime, timedelta
import pprint
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


for d in weatherdata:
    d["awnd"] = d["awnd"] if d["awnd"] is not None else 0

# TODO: The datetime module converts strings into dates fairly easily

weatherdata_dateformat = list(map(
    lambda x : {"date":datetime.fromisoformat(x['date']),
                    **{k: v for k, v in x.items() if k != "date"}
                },
                                weatherdata))
# pprint.pp(weatherdata_dateformat)
# print(type(weatherdata_dateformat[0]["date"]))

# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)
weatherdata_weekday = list(map(lambda x:{"weekday":x["date"].weekday(),**x},weatherdata_dateformat))
#pprint.pp(weatherdata_weekday)

# TODO: what was the warmest weekend day in the dataset?
# warmes_weekend = reduce(lambda acc, x: x if x['weekday'] == 5 or x['weekday'] == 6 and x['tmax'] > acc['tmax'] else acc,
#                         weatherdata_weekday)
# pprint.pp(warmes_weekend)

# tmax_weekend = max(filter(lambda x:x['weekday']==5 or x['weekday']==6, weatherdata_weekday),key=lambda y: y['tmax'])
# pprint.pp(warmes_weekend)

# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
# coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
# coldest_date = date.fromisoformat(coldest_day['date'])
# print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

coldest_day = min(weatherdata_dateformat, key = lambda x:x['tmin'])

# TODO: Look up the next 7 days
# avg_temp = 0
# next = coldest_day['date']
# for i in range(7):
#     next += timedelta(days=1)
#     next_day = list(filter(lambda x:x['date']==next, weatherdata_dateformat))
#     avg_temp += (next_day[0]['tmin']+next_day[0]['tmax'])/2

# average_temp_next_days = avg_temp / 7
# print(f'Average temperature over the next 7 days from the coldest day is {average_temp_next_days}')


# TODO: USe reduce() function to determine the most miserable day in the dataset: 
# largest score = (average wind speed + prcp*10 + max_temp*0.8)/3

most_miserable_day = reduce(
    lambda acc, x:x if (x['awnd'] + x['prcp']*10 + x['tmax']*0.8) > (acc['awnd'] + acc['prcp']*10 + acc['tmax']*0.8) else acc, weatherdata)

print('The most miserable day in the dataset:')
pprint.pp(most_miserable_day) 