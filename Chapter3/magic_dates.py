# File: magic_dates.py
# Description: Magic Dates
# Assignment Name and Number: #6 of Chapter 3
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

month = int(input("Enter a month in number format: "))
day = int(input("Enter a day in number format: "))
year = int(input("Enter a two digit year: "))

date = f"{month}/{day}/{year}"

if year == month * day:
    print(f"{date}")
    print("This date is magic")
else:
    print(f"{date}")
    print("This date is NOT magic")