# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("Start\\Ch_3\\largequakes.csv", "r") as f:
    reader = csv.reader(f)
    sniffer = csv.Sniffer()
    sample = f.read(1024)
    f.seek(0)
    if sniffer.has_header(sample):
        next(reader)

    for row in reader:
        # sol1
        a, b, c, d = row
        result.append({"place": a, "magnitude": b, "date": c, "link": d})

pprint.pp(result)
