# -*- coding: utf-8 -*-
import pandas
from pandas import read_csv
import csv
import matplotlib.pyplot as plt

# data = pandas.read_csv(filepath_or_buffer="weather_data.csv", sep=';')

list_one = []
list_two = []
list_three = []
with open('ogrsech123.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        list_one.append(row[0].split(sep=';'))

for num in list_one:
    list_two = [
        num[0],
        num[1],
        num[2]
    ]
    list_three.append(list_two)
list_three.insert(0, ['sech', 'time', 'P'])

with open('csv_test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    for row in list_three:
        list_ = [row[0], row[1], row[2]]
        writer.writerow(list_)
        print(f'{row[0]},{row[1]},{row[2]}')



data = pandas.DataFrame(list_three)
print(data)
data2 = pandas.read_csv('csv_test.csv')
data2.plot(x='time', y='P')
plt.show()

# data = pandas.read_csv(filepath_or_buffer='ogrsech123.csv', encoding="utf-8")
# # data2 = pandas.read_csv(filepath_or_buffer="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# print(data)
# #
# t_cr = 0
# temp_list = data['temp'].to_list()
# average = sum(temp_list) / len(temp_list)
#
# # print(average)
# #
# # print(data['temp'].mean())
# #
# # print(data['temp'].max())
# # print(max(data['temp']))
#
# # print(data.condition)
#
# # print(data[data.day == 'Monday'])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday)
# print(monday_temp)
# print(monday_temp_F)
#
# data_dict_two = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_ = pandas.DataFrame(data_dict_two)
# print(data_)

# data = pandas.read_csv(filepath_or_buffer="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
