# File: nested_loops_pattern.py
# Description: Program that uses nested loops to make a pattern
# Assignment Name and Number: #14 of Chapter 4
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.


r = 7
for i in range(r, 0, -1):
    print()
    for j in range(i):
        print('* ', end='')