# File: planting_grapevines.py
# Description: Planting Grapevines
# Assignment Name and Number: #13 of Chapter 2
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

R = float(input("Enter the length of the row, in feet: "))
E = float(input("Enter amount of space used by an end-post assembly: "))
S = float(input("Enter the amount of space you would like to have between the vines, in feet: "))

V = (R - (2 * E)) / S

print("Number of grapevines that will fit in a row: ", V)
