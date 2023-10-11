# File: number_analyser.py
# Description: Number Analyser
# Assignment Name and Number: #1 of Chapter 3
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.


Z = "zero"
P = "positive"
N = "negative"
O = "odd"
E = "even"

integer = int(input("Enter a random number: "))

if integer > 0:
    print(f"{integer} is a {P} number")
elif integer < 0:
    print(f"{integer} is a {N} number")
elif integer == 0:
    print(f"{integer} is a {Z} number")

if (integer % 2) == 0:
    print(f"{integer} is {E}")
else:
    print(f"{integer} is {O}")