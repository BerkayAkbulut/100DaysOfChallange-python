# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     tempatures = []
#     for row in data:
#         tempatures.append(row[1])
#     tempatures.pop(0)
#     print(tempatures)

import pandas

data = pandas.read_csv("weather_data.csv")
degrees = data["temp"]
sum = degrees.sum()
len = degrees.count()

print("----------------")
mean = data["temp"].mean()  # same and short way
max = data["temp"].max()

print("----------------")
print(f"Max temp value: {max}")
print(f"Average temp: {sum / len} ")

print("----------------")
monday = data[data.day == "Monday"]
print(f"Chosen day: {monday}")

print("----------------")
most_hot_day2=data[data.temp == data.temp.max()]

print(f"Most Hot Day: {most_hot_day2}")
