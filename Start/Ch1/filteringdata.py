# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snowsdays = list(filter(lambda x:x["snow"] > 0, weatherdata))


# TODO: pretty-print the resulting data set
# pprint.pp(snowsdays)


# filter can also be used on non-numerical data, like strings
# # TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    sommerdays = ['-07-','-08-']
    if any([m in d["date"] for m in sommerdays ]) and d["prcp"] > 0:
        return True
    return False

rainy_sommer_days = filter(lambda x:is_summer_rain_day(x), weatherdata)
# pprint.pp(rainy_sommer_days)