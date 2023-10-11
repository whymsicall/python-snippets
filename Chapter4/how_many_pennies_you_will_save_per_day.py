# File: how_many_pennies_you_will_save_per_day
# Description: How many pennies you will save per day
# Assignment Name and Number: #7 of Chapter 4
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

pennies = 0.01

days = int(input("Enter the number of days: "))

output = "\nDay\tPay\n" \
         "------------------\n"

total_pay = 0.0
day_pay = 0.0

for day in range(days):
    day_pay = pennies
    output += format(day + 1) + "\t$" + format(day_pay, '.2f') + "\n"
    total_pay += day_pay
    pennies *= 2

output += "-----------------------\n" \
        "total pay = $" + format(total_pay, '.2f') + "\n"

print(output)