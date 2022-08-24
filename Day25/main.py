import csv

with open("weather_data.csv") as data_file:
    data=csv.reader(data_file)
    tempatures = []
    for row in data:
        tempatures.append(row[1])
    tempatures.pop(0)
    print(tempatures)