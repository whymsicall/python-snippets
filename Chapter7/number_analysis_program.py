# File: number_analysis_program.py
# Description: Number Analysis Program
# Assignment Name and Number: #4 of Chapter 7
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

from statistics import mean
max_numbers = 20

numbers = []
total_numbers = 0

for i in range(max_numbers):
    inp = int(input("What number would you like to input: "))
    numbers.append(inp)
    total_numbers += inp

avg_numbers = mean(numbers)
max_num = max(numbers)
min_num = min(numbers)

print('total numbers:', total_numbers)
print('average number in the numbers:', avg_numbers)
print('mac number in the numbers:', max_num)
print('min number in the numbers:', min_num)