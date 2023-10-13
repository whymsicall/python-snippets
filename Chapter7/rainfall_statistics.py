# File: rainfall_statistics.py
# Description: Rainfall Statistics
# Assignment Name and Number: #3 of Chapter 7
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.
from statistics import mean

months = ['Janruary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
num_months = 12
current_month = months[1]
rainfall = []
change = 0
total_rain = 0
reflist = []

for i in range(num_months):
    current_month = months[change]
    reflist.append(current_month)
    print('what was the total rainfall in', current_month)
    inp = int(input("total rainfall: "))
    reflist.append(inp)
    rainfall.append(inp)
    change = change + 1
    total_rain += inp

avg_rain = mean(rainfall)
print(reflist)
max_rain = max(rainfall)
min_rain = min(rainfall)
max_month_range = (((rainfall.index(max(rainfall)))+1)*2)-2
min_month_range = (((rainfall.index(min(rainfall)))+1)*2)-2

print('total rainfall throughout the year:', total_rain)
print('the average rainfall thoughout the year:', avg_rain)
print('the month with the most rainfall:', reflist[max_month_range], 'with a rainfall of', max_rain)
print('the month with the least rainfall:', reflist[min_month_range], 'with a rainfall of', min_rain)