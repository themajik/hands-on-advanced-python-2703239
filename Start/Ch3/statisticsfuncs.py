# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
mean_tmin = statistics.mean(x['tmin'] for x in weatherdata)
mean_tmax = statistics.mean(x['tmax'] for x in weatherdata)
# print(f'Mean of tmin is {mean_tmin}')
# print(f'Mean of tmax is {mean_tmax}')



# TODO: calculate the median values for min and max temperatures
median_tmin = statistics.median(x['tmin'] for x in weatherdata)
median_tmax = statistics.median(x['tmax'] for x in weatherdata)
# print(f'Median of tmin is {median_tmin}')
# print(f'Median of tmax is {median_tmax}')

# TODO: use the standard deviation function to find outlier temperatures
standard_deviation_tmin = statistics.stdev(x['tmin'] for x in weatherdata)
standard_deviation_tmax = statistics.stdev(x['tmax'] for x in weatherdata)

outlier_high = mean_tmax + 2*standard_deviation_tmax
outlier_low = mean_tmin - 2*standard_deviation_tmin

outlier_high_days = list(filter(lambda x:x['tmax']>outlier_high, weatherdata))
outlier_low_days = list(filter(lambda x:x['tmin']<outlier_high, weatherdata))

pprint.pp(outlier_high_days)
print('---------------')
pprint.pp(outlier_low_days)