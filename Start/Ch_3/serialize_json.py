# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a JSON file

import json
import datetime


# read in the contents of the JSON file
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6


# TODO: define a function to transform complex JSON to simpler JSON
def simplequake(q):
    p = q["properties"]
    return {
        "place": p["place"],
        "mag": p["mag"],
        "link": p["url"],
        "date": str(datetime.date.fromtimestamp(p["time"] // 1000)),
    }


# filter the data to only include large quakes
largequakes = list(filter(isbig, data["features"]))
# TODO: transform the data to a JSON format we want to save
largequakes = list(map(simplequake, largequakes))

# TODO: use the dumps() function to write json to a string
s = json.dumps(largequakes, sort_keys=True, indent=4)
print(s)
# TODO: use the dump() function to write json to a file
with open(".\\Start\\Ch_3\\largequakes.json", "w", newline="") as c:
    json.dump(largequakes, c, sort_keys=True, indent=4)
