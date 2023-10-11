# File: circle_measurements.py
# Description: Circle Measurements
# Assignment Name and Number: #9 of Chapter 2
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

print('Radius =', radius)
print('Area =', area)
print('Circumference =', circumference)