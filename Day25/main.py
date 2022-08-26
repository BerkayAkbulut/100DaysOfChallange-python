import pandas as pd

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
# print(cinnamon)
gray=len(data[data["Primary Fur Color"]=="Gray"])
# print(gray)
black=len(data[data["Primary Fur Color"]=="Black"])
# print(black)

data_dict={
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray,cinnamon,black]
}
data_csv=pd.DataFrame(data_dict).to_csv()
print(data_csv)