# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
# 1: How many quakes are there in total?
print(f"Total quakes: {data['metadata']['count']}")


# 2: How many quakes were felt by at least 100 people?
feltreports = list(
    filter(
        lambda x: x["properties"]["felt"] is not None
        and x["properties"]["felt"] >= 100,
        data["features"],
    )
)
print(f"At least 100 people: {len(feltreports)}")


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getfelt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0


mostfeltquake = max(data["features"], key=getfelt)
print(
    f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}"
)


# 4: Print the top 10 most significant events, with the significance value of each
def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0


print()
sigevents = sorted(data["features"], key=getsig, reverse=True)
print("<<<The 10 most significant events>>>")
for i in range(0, 10):
    print(
        f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}"
    )
