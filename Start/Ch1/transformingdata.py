# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    f = 0 if f is None else f
    return (f - 32) * 5/9


def ToMM(i):
    i = 0 if i is None else i
    return i * 25.4


def ToKPH(s):
    s = 0 if s is None else s
    return s * 1.60934


def ToMetric(wd):
    copy_wd = copy.copy(wd)
    copy_wd["tmin"] = ToC(wd["tmin"])
    copy_wd["tmax"] = ToC(wd["tmax"])
    copy_wd["prcp"] = ToMM(wd["prcp"])
    copy_wd["snow"] = ToMM(wd["snow"])
    copy_wd["awnd"] = ToKPH(wd["awnd"])
    return copy_wd


# TODO: Use map() to call ToMetric and convert weatherdata to metric
weatherdata_metric = list(map(ToMetric,weatherdata))
# pprint.pp(weatherdata[0])
# pprint.pp(weatherdata_metric[0])

# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0
def avg_temp_to_text(t):
    return "Hot" if t >= 80 else "Warm" if t > 60 and t < 80 else "Cold"

# tuple = list(map(lambda x:(x["date"],Avg_Temp(x["tmin"], x["tmax"])),weatherdata))
tuple = list(map(lambda x:(x["date"], avg_temp_to_text(Avg_Temp(x["tmin"],x["tmax"]))), weatherdata))
pprint.pp(tuple)
