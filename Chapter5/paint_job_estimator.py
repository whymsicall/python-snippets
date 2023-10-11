# File: paint_job_estimator.py
# Description: Paint Job Estimator
# Assignment Name and Number: #8 of Chapter 5
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

sqft = int(input("how many square feet of wall do you need painted: "))
paint_price = int(input("price of paint: "))

req_gallons = sqft / 112
labor_time = (sqft / 112) * 8

pay_per_hour = labor_time * 35
TPgallon = pay_per_hour * req_gallons

total_cost = pay_per_hour + TPgallon

print(f"The number of galones of paint required is: {req_gallons}" )
print(f"The hours of labor required is: {labor_time}")
print(f"The cost of paint required is: {TPgallon}")
print(f"The cost of of labor required is: {pay_per_hour}")
print(f"The total cost is: {total_cost}")