# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

# TODO: Create the header and row structures for the data
header = ["Place", "Magnitude", "Link", "Date"]
rows = []
# TODO: populate the rows with the resulting quake data
for q in largequakes:
    d = datetime.date.fromtimestamp(q["properties"]["time"] // 1000)
    p = q["properties"]
    rows.append([p["place"], p["mag"], p["url"], d])

# TODO: write the results to the CSV file
with open(".\\Start\\Ch_3\\largequakes.csv", "w", newline="") as c:
    writer = csv.writer(c, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
