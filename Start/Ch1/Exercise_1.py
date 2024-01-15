import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

for d in weatherdata:
    d["awnd"] = d["awnd"] if d["awnd"] is not None else 0

# pprint.pp(weatherdata[:3])



result = list(filter(lambda x:(x["snow"]>=0.7 or x["prcp"]>=0.7) and x["tmin"] <= 45 
                    and x["awnd"] >= 10, weatherdata))
pprint.pp(result)
    
# test = weatherdata["snow"]
# pprint.pp(weatherdata)
# type_set = set(type(d["awnd"]) for d in weatherdata)

#print(len(type_set))
#print(ts for ts in type_set)
#print(f'Unique data types of {type_set}')
# inspection = [record for record in weatherdata if record["awnd"] is None]
# pprint.pp(inspection)
