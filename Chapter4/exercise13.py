# File: <exercise13>
# Description: <Population>
# Assignment Name and Number: #13 of Chapter 4
#
# Name: <Landon Svatek>
# GitHub: <whymsicall>
#
# On my honor, <Landon Svatek>, this programming assignment is my own work
# and I have not provided this code to any other student.

start = int(input("Starting number of organisms: "))
increase = int(input("Average daily increase: "))
multiplydays = int(input("Number of days to multiply: "))

print("Days Appox. \tPopulation")

for x in range(1, multiplydays+1):
    if x > 1:
        increasing = start * increase /100
        start += increasing

    print(x,"\t\t\t", format(start, '.2f'))




output = "\nDay Approx.\tPopulation\n" \
         "------------------\n"