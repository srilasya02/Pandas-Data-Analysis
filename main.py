# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     print(data)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd
# data=pd.read_csv("weather_data.csv")
# #print(type(data))
# #print(data["temp"])
# #print(data.to_dict())
# temp_list=data["temp"].to_list()
# print(temp_list)
# n=len(temp_list)
#
# # sum=0
# # for i in range(len(temp_list)):
# #     sum=sum+temp_list[i]
# #
# # avg=sum/n
# # print(avg)
#
# print(data["temp"].max())
# print(data[data.day=="Monday"])
#
# print(data[data.temp==data.temp.max()])
#
# monday=data[data.day=="Monday"]
#
# print(monday.temp)
#
# #creating data frame from scratch
#
# data_dict={
#     "students":["a","b","c"],
#     "scores":[1,2,3]
# }
#
# data1=pd.DataFrame(data_dict)
# data1.to_csv("new_data.csv")

import pandas as pd
data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirell=len(data[data["Primary Fur Color"]=="Gray"])
print(gray_squirell)
black_squirell=len(data[data["Primary Fur Color"]=="Black"])
Cinnamon_squirell=len(data[data["Primary Fur Color"]=="Cinnamon"])

dict={
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[gray_squirell,Cinnamon_squirell,black_squirell]

}

df=pd.DataFrame(dict)
print(df)



