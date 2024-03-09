import csv

country_codes = {}

filename = "countries.csv"

with open("countries.csv", "w") as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        country_codes[line[0]] = line[1]

print(country_codes)
print(country_codes["UA"])