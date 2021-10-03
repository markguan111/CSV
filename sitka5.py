import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_file_s = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file_s = csv.reader(open_file_s, delimiter=",")

header_row = next(csv_file)
header_row_s = next(csv_file_s)
#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)
# testing to conver date from string
# mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(type(mydate))

highs = []
dates = []
lows = []
highs_s = []
dates_s = []
lows_s = []


for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(the_date)




for row in csv_file_s:
    try:
        the_date1 = datetime.strptime(row[2], '%Y-%m-%d')
        high1 = int(row[5])
        low1 = int(row[6])
    except ValueError:
        print(f"Missing data for {the_date1}")
    else:
        highs_s.append(int(row[5]))
        lows_s.append(int(row[6]))
        dates_s.append(the_date1)

# print(highs)
# print(dates)

fig = plt.figure()

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()


# plt.subplot(row,col,index)
#open_file_s = open("sitka_weather_2018_simple.csv", "r")

for row in open_file_s:
          Name1 = row[1]
            
plt.subplot(2, 1, 1)
plt.title(Name1)
plt.xlabel("", fontsize=12)
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates_s, highs_s, c="red", alpha=0.5)
plt.plot(dates_s, lows_s, c="blue", alpha=0.5)

plt.fill_between(dates_s, highs_s, lows_s, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()



Name2 =[]
for row in open_file_s:
          Name2.append
plt.subplot(2, 1, 2)
plt.title(Name2)
plt.xlabel("", fontsize=12)
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()




plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

plt.show()


