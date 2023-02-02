# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
#
# # get data in column
# print(data.temp)
# print(data["temp"])
#
# get data in row
# print(data[data.temp == data.temp.max()])

# tuesday = data[data.day == "Tuesday"]
# tuesday_temp = int(tuesday.temp)
# print(tuesday.temp)

#create a dataframe
data_dict = {
    "students": ["Aloe", "Khoi", "Jeffrey"],
    "scores": [0, 100, 97]
}
data = pandas.DataFrame(data_dict)
data.to_csv("test_scores.csv")


