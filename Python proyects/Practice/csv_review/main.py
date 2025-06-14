import csv
import pandas

csv_input = "./Python Basics/weather/weather_data.csv"

# manually:
# with open(csv_input, "r") as data:
#     csv_reader = data.readlines()

# print(csv_reader)


#This one takes the list but returns a list with just the position marked (we can't use int() with lists)
# with open(csv_input) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1:2]
#         temperatures.append(temp)

# print(temperatures)
        

# This enters into the string of the list and returns teh value
with open(csv_input) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
        
# Same results as previesly but optimized
with open(csv_input) as data_file:
    data = csv.reader(data_file)
    temperatures = [int(row[1]) for row in data if row[1] != "temp" ] # Append row[1] for each {row} in {data} ---> if row[1] that is not "temp" 
    
print(temperatures)
print("\n\n")

# Faster with pandas
data = pandas.read_csv(csv_input)

# data_dict = data.to_dict()
# data_list = data["temp"].to_list()


# # Get a column
# print(data["condition"])
# print(data.condition)

# #doing operations
# print(data["temp"].mean())
# print(data["temp"].max())

# # get a row
# print(data[ data.day == "Monday"])

# get row with condition (hottest day)
# print(data [data.temp == data.temp.max()])
print(data [data["temp"] == data["temp"].max()])


monday = data[data.day == "Monday"]

print((monday.temp * 9/5)+ 32)