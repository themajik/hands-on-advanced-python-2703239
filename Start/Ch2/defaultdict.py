# Example file for Advanced Python: Hands On by Joe Marini
# Count items using a default dictionary

import json
import pprint
from collections import defaultdict


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# The defaultdict collection provides a cleaner way of initializing key values
# TODO: Count the number of data points for each year we have data
#Without using defaultdict
# years = {}
# for d in weatherdata:
#     key = d["date"][0:4]
#     if key in years:
#         years[key] += 1
#     else:
#         years[key] = 1

#using defaultdict
# years = defaultdict(int)
# for d in weatherdata:
#     key = d["date"][0:4]
#     years[key] += 1
# pprint.pp(years)

# TODO: defaultdict can use more complex objects, like lists
# years = defaultdict(list)
# for d in weatherdata:
#     key = d["date"][0:4]
#     years[key].append(d["date"])
# pprint.pp(years)

# TODO: create a dictionary with year-month keys and lists for each day in the month
year_months = defaultdict(list)
for d in weatherdata:
    key = d["date"][0:7]
    year_months[key].append(d)
pprint.pp(len(year_months))

# What were the coldest and warmest days of each month?
def warmest_day(month):
    wd = max(month, key=lambda d: d['tmax'])
    return (wd['date'], wd['tmax'])

def coldest_day(month):
    cd = min(month, key=lambda d: d['tmin'])
    return (cd['date'], cd['tmin'])


# TODO: loop over the keys of the dictionary and find each warmest and coldest day
# for month, daylist in year_months.items():
#    print(f"Warmest day in {month}: {warmest_day(daylist)}")
#    print(f"Coldest day in {month}: {coldest_day(daylist)}")
# pprint.pp(year_months)

summary = defaultdict(list)

for month, daylist in year_months.items():
    key = month
    summary[month].append(dict(Coldest = coldest_day(daylist)))
    summary[month].append(dict(Warmest = warmest_day(daylist)))

pprint.pp(summary)